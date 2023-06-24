#!/usr/bin/python3
""" holds class State"""
import models
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ class state that is inherited from basemdel and base"""
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if models.storage_type == 'db':
        cities = relationship("City", cascade="all, delete", backref="state")

    else:
        @property
        def cities(self):
            """getter for list of city instances related to the state"""
            city_list = []
            all_cities = models.storage.all(City)
            for city in all_cities.values():
                if city.state_id == self.id:
                    city_list.append(city)

            return city_list
