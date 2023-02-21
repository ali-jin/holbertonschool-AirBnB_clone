#!/usr/bin/python3
"""
Module containing the class City
"""
from models.base_model import BaseModel


class City(BaseModel):
    """ Define the City class and inherits from BaseModel """
    state_id = ""
    name = ""
