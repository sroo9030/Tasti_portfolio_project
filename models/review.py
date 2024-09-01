#!/usr/bin/python
"""Review model"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer

class Review(BaseModel, Base):
    """Representation of Review """
    __tablename__ = 'reviews'
    recipe_id = Column(String(60), ForeignKey('recipes.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    number_of_stars = Column(Integer(), nullable=False)

    def __init__(self, *args, **kwargs):
        """initializing"""
        super().__init__(*args, **kwargs)
