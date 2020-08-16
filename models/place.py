#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship, backref
from os import getenv

class Place(BaseModel):
    """ A place to stay """
    __tablename__ = 'places'
    #only if db is selected
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        city_id = Column(String(60),ForeignKey('cities.id'), nullable=False)
        
        user_id = Column(String(60), ForeignKey('user.id'), nullable=False)
        
        name = Column(String(128), nullable=False)
        
        description = Column(String(1024), nullable=True)
        
        #optional params
        number_rooms = Column(Integer, nullable=False, default=0)
        
        number_bathrooms = Column(Integer, nullable=False, default=0)
        
        max_guest = Column(Integer, nullable=False, default=0)
        
        price_by_night = Column(Integer, nullable=False, default=0)
        
        latitude = Column(Float, nullable=True)

        longitude = Column(Float, nullable=True)
        
        places = relationship("Place", backref="user", cascade="all, delete")

    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []
