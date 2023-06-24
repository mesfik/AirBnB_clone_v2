#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, ForeignKey
import models
from models.place import Place


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    if models.storage_type == "db":
        __tablename__ = "cities"

        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'))
        state = relationship('State', back_populates='cities')
        places = relationship('Place', cascade='all, delete-orphan',
                              backref='cities')
    else:
        name = ""
        state_id = ""
