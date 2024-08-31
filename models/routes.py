#!/usr/bin/python
''' 
routes module
'''
from models import app
from flask import render_template, url_for,flash,redirect


@app.route('/')
@app.route('/home')
def home():
    title = "Home"
    return render_template('main.html', title=title)

