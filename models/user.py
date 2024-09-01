#!/usr/bin/python3
"""
user model
"""
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column


class User(BaseModel, Base):
    """User Class"""
    __tablename__ = 'users'
    username = Column(String(128), nullable=False)
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)

    def __init__(self, *args, **kwargs):
        """Constructor"""
        super().__init__(*args, **kwargs)
