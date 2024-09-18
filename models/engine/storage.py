#!/usr/bin/python3
"""
database storage operations
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models.base_model import Base
from models.user import User
from models.review import Review
from models.recipe import Recipe

classes = {
    'User': User,
    'Review': Review,
    'Recipe': Recipe
}


class TheStorage:
    """Database storage class"""
    __engine = None
    __session = None

    def __init__(self):
        """Constructor"""
        MYSQL_USER = 'tasti_user'
        MYSQL_PWD = 'tasti_pwd'
        MYSQL_HOST = 'localhost'
        MYSQL_DB = 'tasti_db'
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(MYSQL_USER,
                                             MYSQL_PWD,
                                             MYSQL_HOST,
                                             MYSQL_DB),pool_pre_ping=True)

    def all(self, cls=None, offset=None, limit=None):
        """Query on the current database session with optional pagination"""
        new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                query = self.__session.query(classes[clss])
                
                # Apply offset and limit for pagination if provided to the query obj:
                if offset is not None:
                    query = query.offset(offset)
                if limit is not None:
                    query = query.limit(limit)

                objs = query.all()  # This is the method that actually executes the query and retrieves the results.
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return new_dict

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """reloads data from the database"""
        # Base.metadata.drop_all(self.__engine)
        Base.metadata.create_all(self.__engine) #  it won't update or modify existing tables just create the new tables. 
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session

    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.remove()

    def get(self, cls, id=None, username=None, email=None, user_id=None):
        """A method to retrieve one object"""
        for obj in self.all(cls).values():  # Assuming all(cls) returns a dict-like object
            if (id is not None and getattr(obj, 'id', None) == id) or \
            (username is not None and getattr(obj, 'username', None) == username) or \
            (email is not None and getattr(obj, 'email', None) == email) or \
            (user_id is not None and getattr(obj, 'user_id', None) == user_id):
                return obj
        return None

    def count(self, cls=None):
        """A method to count the number of objects in storage"""
        if cls:
            counter = len(self.all(cls))
        else:
            counter = len(self.all())
        return counter
