#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship
from models.review import Review
from models.user import User
import models


class Place(BaseModel, Base):
    """ A place to stay """
    if models.storage_type == 'db':
        __tablename__ = 'places'
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, default=0, nullable=False)
        number_bathrooms = Column(Integer, default=0, nullable=False)
        max_guest = Column(Integer, default=0, nullable=False)
        price_by_night = Column(Integer, default=0, nullable=False)
        latitude = Column(Integer, default=0, nullable=False)
        longitude = Column(Integer, default=0, nullable=False)
        cities = relationship("City", back_populates='places')
        user = relationship("User", back_populates='places')

        reviews = relationship('Review', cascade='all, delete-orphan',
                              backref='place')

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
        amenity_ids = []i

        @property
        def reviews(self):
            """Getter attribute that returns the list of Review instances
               with place_id equals to the current Place.id
            """
            review_instances = models.storage.all(models.Review)
            return [review for review in review_instances.values()
                    if review.place_id == self.id]
