#!/usr/bin/python3
"""
recipe model
"""
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column, ForeignKey


class Recipe(BaseModel, Base):
    """User Class"""
    __tablename__ = 'recipes'
    title = Column(String(128), nullable=False)
    content = Column(String(2048), nullable=False)


    def __init__(self, *args, **kwargs):
        """Constructor"""
        super().__init__(*args, **kwargs)
