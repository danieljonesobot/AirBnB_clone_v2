#!/usr/bin/python3
""" this class handles operations in sqlalchemy """
from os import getenv
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
from models.state import State
from models.base_model import Base
from models.city import City
from models.user import User
from models.review import Review
from models.place import Place
from models.amenity import Amenity


class DBStorage:
    """ create tables in environmental"""
    __engine = None
    __session = None

    def __init__(self):
        user = getenv("HBNB_MYSQL_USER")
        passwd = getenv("HBNB_MYSQL_PWD")
        db = getenv("HBNB_MYSQL_DB")
        host = getenv("HBNB_MYSQL_HOST")
        env = getenv("HBNB_ENV")

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, passwd, host, db),
                                      pool_pre_ping=True)

        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """functioni to return a dictionary
        """
        dic = {}
        if cls:
            if type(cls) is str:
                cls = eval(cls)
            query = self.__session.query(cls)
            for elem in query:
                key = "{}.{}".format(type(elem).__name__, elem.id)
                dic[key] = elem
        else:
            lista = [State, City, User, Place, Review, Amenity]
            for clase in lista:
                query = self.__session.query(clase)
                for elem in query:
                    key = "{}.{}".format(type(elem).__name__, elem.id)
                    dic[key] = elem
        return (dic)

    def new(self, obj):
        """adds  new element to the table in the db
        """
        self.__session.add(obj)

    def save(self):
        """save changes to the database
        """
        self.__session.commit()

    def delete(self, obj=None):
        """ function to delete objects
        """
        if obj:
            self.session.delete(obj)

    def reload(self):
        """function to confirgure relaod
        """
        Base.metadata.create_all(self.__engine)
        se_ = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(se_)
        self.__session = Session()

    def close(self):
        """ function to close session
        """
        self.__session.close()
