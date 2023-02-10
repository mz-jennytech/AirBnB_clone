#!/usr/bin/python3
"""Modulde User class
inherits from BaseModel
"""
from models.base_model import BaseModel


class User(BaseModel):
    """ Defines User class
    Attributes
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
