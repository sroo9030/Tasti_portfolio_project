#!/usr/bin/python
'''
create the tables from my models
'''

from models import storage,app
from models.user import User 
from models.review import Review
from models.recipe import Recipe
from models.base_model import Base
with app.app_context():
    ''' access the app_context allow to intract with app and get required config'''

    # create the tables again and the strucure of my models:
    storage.reload()
