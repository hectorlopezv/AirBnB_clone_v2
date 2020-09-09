#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, backref
from os import getenv


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """

    __tablename__ = "states"
    if getenv('HBNB_TYPE_STORAGE') == 'db':

        name = Column(String(128), nullable=False)
        cities = relationship("City", cascade="all, delete", backref="state")

    else:
        name = ""

        @property
        def cities(self):
            """ Returns the list of City"""
            from models import storage
            from models import City
            return [v for k, v in storage.all(City).items()
                    if v.state_id == self.id]
