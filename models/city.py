#!/usr/bin/python3
"""This module conatins the city class"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.place import Place
from sqlalchemy import ForeignKey
from models.base_model import BaseModel, Base

class City(BaseModel, Base):
    """This class represents the City
    """
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    places = relationship("Place", cascade='all, delete, delete-orphan',
                          backref="cities")
