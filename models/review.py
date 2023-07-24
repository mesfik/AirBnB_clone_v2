#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import models


class Review(BaseModel, Base):
    """ Review classto store review information """
    if models.storage_type == 'db':
        __tablename__ = 'reviews'
        text = Column(String(1024), nullable=False)
        place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        place = relationship('Place', back_populates='reviews',
                             overlaps="place_reviews")
        user = relationship('User', back_populates='reviews',
                            overlaps="user_reviews")
    else:
        place_id = ""
        user_id = ""
        text = ""
