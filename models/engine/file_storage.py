#!/usr/bin/python3
"""Module FileStorage"""

import json
from models.base_model import BaseModel
from models.amenity import Amenity
from models.review import Review
from models.place import Place
from models.state import State
from models.user import User
from models.city import City


class FileStorage:
    """Defines FileStorage class that 
    represents an abstracted storage engine.
    Attributes:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id"""
        cl_name = obj.__class__.__name__
        self.__objects["{}.{}".format(cl_name, obj.id)] = obj

    def save(self):
        """Serialize: __objects to the JSON file"""
        my_dict = FileStorage.__objects
        obj_dict = {obj: my_dict[obj].to_dict() for obj in my_dict.keys()}
        with open(self.__file_path, "w") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Deserialize: JSON file __file_path to __objects, if it exists."""
        try:
            with open(self.__file_path) as f:
            obj_dict = json.load(f)
                for obj in obj_dict.values():
                    cls_name = obj["__class__"]
                    del obj["__class__"]
                    self.new(eval(cls_name)(**obj))
        except FileNotFoundError:
            return
