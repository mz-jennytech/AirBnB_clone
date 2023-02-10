#!/usr/bin/python3
"""Module BaseModel
Defines parent of all classes
"""

import models
from uuid import uuid4 as uid
from datetime import datetime as dt


class BaseModel:
    """Defines the BaseModel class module
    Attributes: None
    Methods:
        __init___(self, *args, **kwargs)
        to_dict(self)
        save(self)
        __str__(self)
        __repr__(self)
    """

    def __init__(self, *args, **kwargs):
        """Initialize BaseModel obj and saves
        Args:
            *args: any argument
            **kwargs: key / value pairs of keyworded argument
        Initializes object with attributes:
            id (str): random generated id from uuid4
            updated_at: date and time obj is updated
            created_at: date and time obj is created
            tformat: just variable
        """
        tformat = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for key, val in kwargs.items():
                if key == "created_at":
                    self.created_at = dt.strptime(val, tformat)
                elif key == "updated_at":
                    self.updated_at = dt.strptime(val, tformat)
                elif key == "__class__":
                    pass
                else:
                    setattr(self, key, val)
        else:
            self.id = str(uid())
            self.updated_at = dt.now()
            self.created_at = dt.now()
            model.storage.save()

    def to_dict(self):
        """Returns the dictionary rep of instance """
        dic = {}
        dic["__class__"] = self.__class__.__name__
        for key, val in self.__dict__.items():
            if isinstance(val, (dt, )):
                dic[key] = val.isoformat()
            else:
                dic[key] = val
        return dic

    def save(self):
        """updates instance and saves in serialized file"""
        self.update_at = dt.now()
        model.storage.save()

    def __str__(self):
        """Overrides built-in __str__
        Return string rep or info of model
        """
        s_format = "[{}] ({}) {}"
        c_name = self.__class__.__name__
        return (s_format.format(c_name, self.id, self.__dict__))

    def __repr__(self):
        """Overrides built-in __repr__
        Returns __str__ on model
        """
        return (self.__str__())
