#!/usr/bin/python3
import uuid
from datetime import datetime


class BaseModel:
    """"Class that defines all common
    attributes/methods for other classes
    """
    def __init__(self, id=None, created_at=None, updated_at=None):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        dictionary = self.__dict__.copy()
        dictionary['__class__'] = self.__class__.__name__
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary

    def __str__(self):
        className = self.__class__.__name__
        return "[{}] ({}) {}".format(className, self.id, self.__dict__)
