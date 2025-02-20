#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from models.base_model import BaseModel
from models.state import State
from models.user import User
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from os import getenv


if getenv('HBNB_TYPE_STORAGE') == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
    storage.reload()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
    storage.reload()
