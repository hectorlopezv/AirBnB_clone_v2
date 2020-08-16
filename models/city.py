#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base #alquemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship, backref
from os import getenv


class City(BaseModel, Base):
    """ The city class, contains state ID and name """ 
    __tablename__ = 'cities'
    #only if db is selected
    if getenv('HBNB_TYPE_STORAGE') == 'db':
       
        name = Column(String(128), nullable=False)
        state_id = Column(String(60),  ForeignKey('states.id', ondelete="CASCADE"), nullable=False)
        places = relationship("Place", backref="cities", cascade="all, delete")
    else:#filestorage
        name = ""
        state_id = ""
    """
    if getenv('HBNB_TYPE_STORAGE') == 'db':

        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
        places = relationship("Place", backref="cities", cascade="all, delete")
    else:
        name = ""
        state_id = ""
    """