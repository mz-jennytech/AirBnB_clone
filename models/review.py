#!/usr/bin/python3
"""Module Review Class
Inherits from BaseModel
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Defines Review class attributes"""

    place_id = ""
    user_id = ""
    text = ""
