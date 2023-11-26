#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """ State class which inherit BaseModel and Base"""

    __tablename__ = "states"
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state",
                              cascade="all, delete, delete-orphan")
    else:
        name = ""

    @property
    def cities(self):
        """getter attribute that returns the list of `City`
           with the `state_id` equal to `State.id`
        """
        city_list = []
        all_city = models.storage.all(City)
        for city in all_city.values():
            if city.state_id == self.id:
                city_list.append(city)
        return city_list
