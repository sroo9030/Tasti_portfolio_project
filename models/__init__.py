#!/usr/bin/python3
"""program initialization"""

from models.engine import TheStorage
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from models.user import User  # Import user here

# Initialize components
storage = TheStorage()
storage.reload()
app = Flask(__name__)
app.config['SECRET_KEY'] = 'b54af37ce9b4df9c42b12577ad7fd3fe'
encrypter = Bcrypt(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "Login"

# Move the login_manager decorator here to avoid circular import with models
@login_manager.user_loader
def load_user(user_id):
    from models import storage  # Lazy import to avoid circular import
    return storage.get(User, id=user_id)

# Import routes after initialization to prevent circular import
from models import routes
