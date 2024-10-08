#!/usr/bin/python3
"""
recipe model
"""
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column, ForeignKey,Text
from sqlalchemy.orm import relationship


class Recipe(BaseModel, Base):
    """User Class"""
    __tablename__ = 'recipes'
    title = Column(String(128), nullable=False)
    descripion = Column(String(1024), nullable=False)
    ingradiantes = Column(String(2048), nullable=False)
    instructions = Column(Text, nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    image_name = Column(String(60), nullable=True)
    reviews = relationship('Review', backref='recipe')

    def __init__(self, *args, **kwargs):
        """Constructor"""
        super().__init__(*args, **kwargs)

    @property
    def image_url(self):
        """Generate the full URL for the recipe image"""
        if self.image_name:
            return self.image_name
        return 'default.png'
