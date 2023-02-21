#!/usr/bin/python3
"""
Module containing the class User
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    Class User inherits from BaseModel
    """
    
    email = ""
    password = ""
    first_name = ""
    last_name = ""
