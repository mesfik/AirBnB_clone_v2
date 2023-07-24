#!/usr/bin/python3
"""
The db_storage module
This module defines a class to manage database storage for hbnb clone
"""

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class DBStorage:
    """The database storage engine"""
    __engine = None
    __session = None

    def __init__(self):
        """create the engine (self.__engine)"""
        user = os.getenv("HBNB_MYSQL_USER", default=None)
        password = os.getenv("HBNB_MYSQL_PWD", default=None)
        host = os.getenv("HBNB_MYSQL_HOST", default=None)
        db = os.getenv("HBNB_MYSQL_DB", default=None)
        HBNB_ENV = os.getenv('HBNB_ENV')

        url = "mysql+mysqldb://{}:{}@{}/{}".format(user, password, host, db)
        self.__engine = create_engine(url, pool_pre_ping=True)

        if HBNB_ENV == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session"""
        if cls is not None:
            objects = self.__session.query(cls).all()
            cls_session = {}
            for obj in objects:
                key = "{}.{}".format(type(obj).__name__, obj.id)
                cls_session[key] = obj
            return cls_session
        else:
            all_objects = []
            for cls in BaseModel.__subclasses__():
                objects = self.__session.query(cls).all()
                all_objects.extend(objects)

            all_objects_dict = {}
            for obj in all_objects:
                key = "{}.{}".format(obj.__class__.__name__, obj.id)
                all_objects_dict[key] = obj
            return all_objects_dict

    def new(self, obj):
        """Adds the object to the current database session"""
        if obj:
            if self.__session.object_session(obj) is None:
                self.__session.add(obj)

    def save(self):
        """Saves storage dictionary to file"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Create the current database session (self.__session)
        from the engine (self.__engine)"""

        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(
                sessionmaker(bind=self.__engine, expire_on_commit=False))

    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.remove()
