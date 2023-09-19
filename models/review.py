#!/usr/bin/python3
"""This script contains the Review class"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, Float
from models.base_model import BaseModel, Base


class Review(BaseModel, Base):
    """This class is for Review whcih inherits from the BaseModel or Base
    """
    __tablename__ = "reviews"
    text = Column(String(1024), nullable=False)
    place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
