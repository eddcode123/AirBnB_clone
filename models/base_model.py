#!/usr/bin/python3
""" Base class model """
import uuid
from datetime import datetime


class BaseModel:
    """Defines common attributes/methods for other classes"""

    def __init__(self, *args, **kwargs):
        """Initializes a BaseModel instance"""

        self.updated_at = datetime.now()
        # Update instance attributes if provided in kwargs
        if kwargs:
            # iterate over each attribiute
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()

    def __str__(self):
        """Returns a string representation of the object"""
        class_name = type(self).__name__
        return f'[{class_name}] ({self.id}) {self.__dict__}'

    def save(self):
        """ updates updated_at with the current datetime """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ returns a dict containing all k:v of __dict__ of the instance """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = type(self).__name__
        # Convert 'created_at' and 'updated_at' to ISO format strings
        obj_dict['created_at'] = self.created_at.strftime('%Y-%m-%dT%H:%M:%S.%f')
        obj_dict['updated_at'] = self.updated_at.strftime('%Y-%m-%dT%H:%M:%S.%f')
        return obj_dict
