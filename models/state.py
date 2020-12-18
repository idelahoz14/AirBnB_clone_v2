#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalñchemy import relationship
from models.engine.file_storage import FileStorage
from models.city import City
from os import getenv
from models import storage


class State(BaseModel):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable = False)
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship("City", backref='state', cascade="all, delete, delete-orphan")
    else:
        @property
        def cities(self):
            """ List the cities """
            List = []
            for key, value in storage.all(City).items():
            if self.id == obj.state_id:
                List.append(value)
        return List
