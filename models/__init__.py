#!/usr/bin/python3
""" __init__ file """
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.state import State
from models.user import User
from models.amenity import Amenity
from models.review import Review
from models.place import Place
from os import getenv


if getenv("HBNB_TYPE_STORAGE") == "db":
    storage = DBStorage()
else:
    storage = FileStorage()
storage.reload()
