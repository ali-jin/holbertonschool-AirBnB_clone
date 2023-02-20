#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime

class BaseModel:
    """"Class that defines all common
    attributes/methods for other classes
    """
    def __init__(self, id=None, created_at=None, updated_at=None):
        self.id = uuid4()
        self.created_at = datetime.now().isoformat()
        self.updated_at = datetime.now().isoformat()

    def save(self):
        self.updated_at = datetime.now().isoformat()

    def to_dict(self):
        self.__dict__['__class__'] = self.__class__.__name__
        return self.__dict__

    def __str__(self):
        className = self.__class__.__name__
        return "[{}] ({}) {}".format(className, self.id, self.__dict__)
