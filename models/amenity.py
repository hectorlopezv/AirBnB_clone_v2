#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel,Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float
from sqlalchemy.orm import relationship, backref
from os import getenv


class Amenity(BaseModel, Base):
    """class amenity"""
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    places = relationship("Place", backref="cities", cascade="all, delete")
    
