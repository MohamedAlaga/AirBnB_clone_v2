#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """this is Amenity class"""

    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
    places = relationship("Place", secondary="place_amenity", backref="amenity_places")
