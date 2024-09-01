#!/usr/bin/python
'''
create the tables from my models
'''

from models import db,app

with app.app_context():
    ''' access the app_context allow to intract with app and get required config'''

    # create the tables again and the strucure of my models:
    db.create_all()
