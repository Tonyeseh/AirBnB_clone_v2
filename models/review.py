#!/usr/bin/python3
""" Review module for the HBNB project """
from models import storage
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column, ForeignKey
from sqlalchemy.orm import relationship


class Review(BaseModel, Base):
    """ Review inherits from BaseModel and Base
    """
    __tablename__ = "reviews"
    text = Column(String(1024), nullable=False)
    place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    user = relationship("User", back_populates="reviews")
    place = relationship("Place", back_populates="reviews")


    def __init__(self, *args, **kwargs):
        """ Initialises the State class
            Args:
                args: Not used
                kwargs: dictionary format of the class
        """
        super().__init__(*args, **kwargs)
