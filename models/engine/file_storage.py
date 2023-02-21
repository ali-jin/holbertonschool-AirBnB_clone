#!/usr/bin/python3
""" FileStorage class """
import json
from os import path
from models.base_model import BaseModel


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

        for key, value in FileStorage.__objects.items():
                new_dict.update({key: value.to_dict()})

        with open(self.__file_path, "w", encoding="utf-8") as file:
            file.write(json.dumps(new_dict))

    def reload(self):
        try:
            with open(FileStorage.__file_path, encoding="utf-8") as file:
                new_dict = json.load(file)
                for key, value in new_dict.items():
                    FileStorage.__objects[key] = eval(value["__class__"] + '(**value)')
        except FileNotFoundError:
            pass