#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """"Class that defines all common
    attributes/methods for other classes
    """
    def __init__(self):
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        self.__dict__['__class__'] = self.__class__.__name__
        self.__dict__['created_at'] = self.created_at.isoformat()
        self.__dict__['updated_at'] = self.updated_at.isoformat()
        return self.__dict__

    def __str__(self):
        className = self.__class__.__name__
        return "[{}] ({}) {}".format(className, self.id, self.__dict__)
