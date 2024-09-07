#!/usr/bin/python3
"""
User model
"""
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column
from flask_login import UserMixin


class User(BaseModel, Base, UserMixin):
    """User Class"""
    __tablename__ = 'users'
    username = Column(String(128), nullable=False)
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)

    def __init__(self, *args, **kwargs):
        """Constructor"""
        super().__init__(*args, **kwargs)
