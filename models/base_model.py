#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from models import storage

Base = declarative_base()

class BaseModel:
    """A base class for all hbnb models"""

    id = Column(String(60), primary_key = True)
    created_at = Column(DataTime, nullable =  False, deafault = datetime.utcnow())
    updated_at = Column(DataTime, nullable =  False, deafault = datetime.utcnow())
    
    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if **kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    val = datetime.strptime(value, "%Y-%m-%D-%h:%M:%S.%f")
                    setattr(self, key, val)
                elif not key == '__class__':
                    setattr(self, key, value)
            if self.id is None:
                setattr(self, 'id', str(uuid.uuid4()))
            if self.created_at is None:
                setattr(self, 'created_at', datetime.utcnow())
            if self.updated_at is None
                setattr(self, 'updated_at', datetime.utcnow())
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        if '_sa_instance_state' in dictionary:
            del(dictionary['_sa_instance_state'])
        return dictionary

    def delete(self):
        """ delete the current instance from the storage """
        models.storage.delete(self)
