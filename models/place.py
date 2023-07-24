#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Table
from sqlalchemy.orm import relationship
from models.review import Review
from models.amenity import Amenity
import models


if models.storage_type == 'db':
    place_amenity = Table('place_amenity', Base.metadata,
                          Column('place_id', String(60),
                                 ForeignKey('places.id', onupdate='CASCADE',
                                            ondelete='CASCADE'),
                                 primary_key=True),
                          Column('amenity_id', String(60),
                                 ForeignKey('amenities.id', onupdate='CASCADE',
                                            ondelete='CASCADE'),
                                 primary_key=True))


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
        cities = relationship('City', back_populates='places',
                              overlaps="cities_places")
        user = relationship('User', back_populates='places',
                            overlaps="user_places")

        reviews = relationship("Review", cascade="delete",
                               backref="place_reviews", )
        amenities = relationship("Amenity", secondary="place_amenity",
                                 backref="place_amenities", viewonly=False)
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

        @property
        def reviews(self):
            """Getter attribute that returns the list of Review instances
               with place_id equals to the current Place.id
            """
            review_instances = models.storage.all(models.Review)
            return [review for review in review_instances.values()
                    if review.place_id == self.id]

        @property
        def amenities(self):
            """Getter attribute that returns the list of Amenity instances
               based on the attribute amenity_ids that contains all Amenity.id
               linked to the Place
            """
            amenity_instances = models.storage.all(Amenity)
            return [amenity for amenity in amenity_instances.values()
                    if amenity.id in self.amenity_ids]

        @amenities.setter
        def amenities(self, amenity_obj):
            """Setter attribute that handles append method
            for adding an Amenity.id
            to the attribute amenity_ids.
            This method should accept only Amenity object,
            otherwise, do nothing.
            """
            if isinstance(amenity_obj, Amenity):
                self.amenity_ids.append(amenity_obj.id)
