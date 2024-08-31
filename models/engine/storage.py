#!/usr/bin/python3
"""
database storage operations
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models.base_model import Base
classes = {}


class TheStorage:
    """Database storage class"""
    __engine = None
    __session = None

    def __init__(self):
        """Constructor"""
        MYSQL_USER = 'tasti_user'
        MYSQL_PWD = 'tasti_pwd'
        MYSQL_HOST = '' #server to host in it
        MYSQL_DB = 'tasti_db'
        # MYSQL_USER = getenv('MYSQL_USER')
        # MYSQL_PWD = getenv('MYSQL_PWD')
        # MYSQL_HOST = getenv('MYSQL_HOST')
        # MYSQL_DB = getenv('MYSQL_DB')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(MYSQL_USER,
                                             MYSQL_PWD,
                                             MYSQL_HOST,
                                             MYSQL_DB))

    def all(self, cls=None):
        """query on the current database session"""
        new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return (new_dict)

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
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session

    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.remove()

    def get(self, cls, id):
        """A method to retrieve one object"""
        for obj in self.all(cls).values():
            if obj.id == id:
                return obj
        return None

    def count(self, cls=None):
        """A method to count the number of objects in storage"""
        if cls:
            counter = len(self.all(cls))
        else:
            counter = len(self.all())
        return counter
