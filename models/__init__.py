#!/usr/bin/pyhton3
"""program initialization"""

from models.engine import TheStorage
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt


storage = TheStorage()
storage.reload()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://tasti_user:tasti_pwd@localhost/tasti_db' # important: don't forget to exchange it to enviroment var
db = SQLAlchemy(app)
encrypter = Bcrypt()



# we put it at the last because we don't need circular import again (routes need the app variable)
from models import routes