#!/usr/bin/python
''' 
Routes module
'''

from models import app, encrypter, storage
from flask import render_template, url_for, flash, redirect
from models.forms import RegistrationForm, loginForm, RecipeForm
from models.user import User
from models.recipe import Recipe
from flask_login import login_user, logout_user, login_required, current_user


@app.route('/')
@app.route('/home')
def home():
    title = "Home"
    return render_template('main.html', title=title)


@app.route("/register", methods=['GET', 'POST'])
def register():
    '''Registration route'''
    title = 'Registration'
    form = RegistrationForm()

    if form.validate_on_submit():
        pass_hashed = encrypter.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=pass_hashed)
        storage.new(user)
        storage.save()
        flash(f"Sign up for {form.username.data} was successful! You can now log in.", 'success')
        return redirect(url_for('login'))
    
    return render_template('register.html', title=title, form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    '''Login route, POST for submitting login data'''
    title = 'Log In'
    form = loginForm()
    
    if form.validate_on_submit():
        user = storage.get(User, email=form.email.data)
        if user and encrypter.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)   # use Flask login_user function
            flash(f"{user.username} successfully logged in.", 'success')
            return redirect(url_for('home'))
        else:
            flash("Invalid email or password Please try again.", 'danger')
    
    return render_template('login.html', title=title, form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()  # Use Flask-Login's logout_user function
    return redirect(url_for('login'))


@app.route('/post/new', methods=['GET', 'POST'])
def post():
    if not current_user.is_authenticated:
        return redirect(url_for('login'))
    title = "New recipe"
    form = RecipeForm()
    if form.validate_on_submit():
        recipe = Recipe(title=form.title.data,
                        content=form.content.data,
                        user_id=current_user.id)
        storage.new(recipe)
        storage.save()
        flash('Your recipe has been created!', 'success')
        return redirect(url_for('home'))
    return render_template('new_recipe.html', title='New recipe', form=form)
