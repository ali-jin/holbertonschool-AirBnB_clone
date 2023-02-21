#!/usr/bin/python3
""" FileStorage class """
import json
from os import path


class FileStorage:

    __file_path = "file.json"
    __objects = {}

def all(self):
    return self.__objects

def new(self, obj):
    key = obj.__class__.__name__ + "." + str(obj.id)
    self.__objects[key] = obj

def save(self):
    new_dict = {}

    for key, value in self.__objects.items():
        new_dict[key] = value.to_dict()

        with open(self.__file_path, "w", encoding="utf-8") as file:
            json.dump(new_dict, file)

def reload(self):