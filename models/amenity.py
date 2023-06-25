#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
import models
from sqlalchemy import Column, String, Table, ForeignKey
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    if models.storage_type == 'db':
        __tablename__ = 'amenities'
        name = Column(String(128), nullable=False)
        place_amenities = Table('place_amenities', Base.metadata,
                                Column('place_id', String(60),
                                       ForeignKey('places.id'),
                                       nullable=False, primary_key=True),
                                Column('amenity_id', String(60),
                                       ForeignKey('amenities.id'),
                                       nullable=False, primary_key=True))
        place = relationship('Place', secondary=place_amenities,
                             backref='amenity')
    else:
        name = ""
