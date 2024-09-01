#!/usr/bin/python
'''
create the tables from my models
'''

from models import db,app
from models.user import User 
from models.review import Review
from models.recipe import Recipe

with app.app_context():
    ''' access the app_context allow to intract with app and get required config'''

    # create the tables again and the strucure of my models:
    db.drop_all()
    db.create_all()
