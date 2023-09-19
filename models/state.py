#!/usr/bin/python3
"""This module contains the State class"""
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
import models
from sqlalchemy import Column, Integer, String
import shlex
from models.city import City

class State(BaseModel, Base):
    """This is is the class for state
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade='all, delete, delete-orphan',
                          backref="state")

    @property
    def cities(self):
        all_elm = models.storage.all()
        l_a = []
        res = []
        for key in all_elem:
            city = key.replace('.', ' ')
            city = shlex.split(city)
            if (city[0] == 'City'):
                l_a.append(var[key])
        for item in l_a:
            if (item.state_id == self.id):
                res.append(item)
        return (res)
