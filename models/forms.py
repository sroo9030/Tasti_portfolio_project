#!/usr/bin/python
'''
module contain all the forms of the project
'''

from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from models import encrypter, storage
from models.user import User


class RegistrationForm(FlaskForm):
    '''Registration form'''

    username = StringField("username", 
                           validators=[DataRequired(), Length(min=4, max=20)])

    email = StringField("email", 
                        validators=[DataRequired(), Length(min=8, max=50), Email()])

    password = PasswordField("enter your password", 
                             validators=[DataRequired()])

    confirm_password = PasswordField("confirm your password",
                                     validators=[DataRequired(), EqualTo('password')])

    submit = SubmitField("Sign up")

    def validate_username(self, username):
        ''' validate that the username is unique'''
        user_exist = storage.get(User, username=username.data)
        if user_exist:
            raise ValidationError("This username is already taken. Please choose another one.")
    
    def validate_email(self, email):
        ''' validate that the email is unique'''
        email_exist = storage.get(User, email=email.data)
        if email_exist:
            raise ValidationError("This email is already registered. Please use another one.")


class loginForm(FlaskForm):
    '''Login form'''

    email = StringField("email",
                        validators=[DataRequired(), Length(min=4, max=50), Email()])

    password = PasswordField("enter your password", 
                             validators=[DataRequired()])

    remember = BooleanField("Remember me")
    submit = SubmitField("LOG IN")

    def validate_correct_info(self):
        ''' check if the password is correct'''
        user_exist = storage.get(User, email=self.email.data)
        if user_exist is None or not encrypter.check_password_hash(user_exist.password, self.password.data):
            raise ValidationError("Your email or password is incorrect.")


class RecipeForm(FlaskForm) :
    '''adding a new recipe form'''
    title = StringField('Title', validators=[DataRequired(), Length(max=128)])
    descripion = TextAreaField(' descripion', validators=[DataRequired(), Length(max=2048)])
    ingradiantes = TextAreaField('ingradiantes', validators=[DataRequired(), Length(max=2048)])
    instructions = TextAreaField('instructions', validators=[DataRequired(), Length(max=2048)])
    picture = FileField('Upload a picture', validators=[FileAllowed(['jpg', 'jpeg', 'png'])])
    submit = SubmitField('Submit')
