#!/usr/bin/python
''' 
routes module
'''
from models import app,encrypter,db
from flask import render_template, url_for,flash,redirect
from models.forms import RegistrationForm, loginForm
from models.user import User


@app.route('/')
@app.route('/home')
def home():
    title = "Home"
    return render_template('main.html', title=title)


@app.route("/register", methods=['GET', 'POST'])
def register():
    '''registeration route'''
    title = 'registeraion'
    form = RegistrationForm()

    if form.validate_on_submit() and form.validate_username(form.username.data) and form.validate_email(form.email.data):
        pass_hashed = encrypter.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=pass_hashed)
        db.session.add(user)
        db.session.commit()
        flash(f"sign up for {form.username.data} has done seccessfully you can now login", 'success')
        return redirect(url_for('login'))
    # flash(f"sorry {form.username.data} something went wrong !!", 'danger')
    return render_template('register.html', title=title, form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    '''log in route, the methods for route is to allow post data'''
    title = 'LOG IN'
    form = loginForm()
    if form.validate_on_submit() and form.validate_correct_info() is True:
        flash(f"{form.email.data} seccessfully loged in", 'success')
        return redirect(url_for('home'))
    return render_template('login.html', title=title, form=form)