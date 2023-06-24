#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), nullable=False, foreign_key('states.id'))

    if models.storage_type == 'db':
        state = relationship('State', back_populates='cities')
        places = relationship('Place', back_populates='city')
    else:
        name = ""
        state_id = ""
