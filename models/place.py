#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship, backref
from os import getenv
from models.amenity import Amenity



class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"


    place_amenity = Table ('place_amenity', Base.metadata,
                Column('place_id', String(60), ForeignKey('places.id'), primary_key=True, nullable=False),
                Column('amenity_id', String(60),ForeignKey('amenities.id'), primary_key=True, nullable=False)
            )
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship("Review", backref="place", cascade="all, delete")
        amenities = relationship("Amenity", secondary=place_amenities, backref="place_amenities" ,viewonly=False)
    else:
        
        @property
        def reviews(self):
            """Return list of review instances for file storage
            matching place_id
            """
            from models import storage
            return {k: v for k, v in storage.all().items() if v.place_id == self.id}
        @property
        def amenities(self):
            """Return list of review instances for file storage
            matching place_id
            """
            from models import storage
            return {k: v for k, v in storage.all().items() if type(v) == Amenity if v.id in Place.amenity_ids}
        
        @amenities.setter
        def amenities(self, val):
            if type(val) != Amenity:
                return
            Place.amenity_ids += val.id
    
    #only if db is selected
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        city_id = Column(String(60),ForeignKey('cities.id', ondelete="CASCADE"), nullable=False)
        
        user_id = Column(String(60), ForeignKey('users.id', ondelete="CASCADE"), nullable=False)
        
        name = Column(String(128), nullable=False)
        
        description = Column(String(1024), nullable=True)
        
        #optional params
        number_rooms = Column(Integer, nullable=False, default=0)
        
        number_bathrooms = Column(Integer, nullable=False, default=0)
        
        max_guest = Column(Integer, nullable=False, default=0)
        
        price_by_night = Column(Integer, nullable=False, default=0)
        
        latitude = Column(Float, nullable=True)

        longitude = Column(Float, nullable=True)
        amenity_ids = []
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
