#!/usr/bin/python3
"""DBStorage, the New Engine"""
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import Base
from sqlalchemy.orm import sessionmaker, scoped_session
import models
from models.city import City
from models.user import User
from models.amenity import Amenity
from models.state import State
from models.place import Place
from models.review import Review


class DBStorage:
    """class Database Storage using sqlalchemy"""

    __engine = None
    __session = None

    def __init__(self):
        """Initializing the new engine"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(getenv('HBNB_MYSQL_USER'),
                                             getenv('HBNB_MYSQL_PWD'),
                                             getenv('HBNB_MYSQL_HOST'),
                                             getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """method to query the database"""

        cls_dict = {}
        classes = [State, City, User, Place, Review, Amenity]

        if cls is None or cls == "":
            for cls_name in classes:
                query = self.__session.query(cls_name)
                for val in query:
                    key = "{}.{}".format(val.__class__.__name__, val.id)
                    cls_dict[key] = val
            return cls_dict
        else:
            query = self.__session.query(cls)
            for val in query:
                key = "{}.{}".format(val.__class__.__name__, val.id)
                cls_dict[key] = val
            return cls_dict

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
        """create all tables in the database"""

        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """close scoped session"""
        self.__session.remove()
