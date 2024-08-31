#!/usr/bin/python3
"""
basemodel identification
"""
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from uuid import uuid4
from sqlalchemy import Column, String, DateTime


Base = declarative_base()


class BaseModel:
    """BaseModel Class"""
    id = Column(String(60), primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow())
    updated_at = Column(DateTime, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Constructor"""
        if kwargs:
            tt = '%Y-%m-%dT%H:%M:%S.%f'
            for k, v in kwargs.items():
                if k != '__class__':
                    setattr(self, k, v)
            if kwargs.get('created_at') and type(self.created_at) is str:
                self.created_at = datetime.strptime(kwargs['created_at'], tt)
            else:
                self.created_at = datetime.utcnow()
            if kwargs.get('updated_at') and type(kwargs['updated_at']) is str:
                self.updated_at = datetime.strptime(kwargs['updated_at'], tt)
            else:
                self.updated_at = datetime.utcnow()
            if kwargs.get('id') is None:
                self.id = str(uuid4())
        else:
            self.id = str(uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = self.created_at

    def save(self):
        """updates the attribute 'updated_at' with the current datetime"""
        from models import storage
        self.updated_at = datetime.utcnow()
        storage.new(self)
        storage.save()

    def delete(self):
        from models import storage
        """delete from storage"""
        storage.delete(self)
