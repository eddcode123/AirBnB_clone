#!/usr/bin/python3
""" File storage Method """
import json


class FileStorage():
    """ Defines a Filestorage engine

    Args:
    __file_path (str): string - path to the JSON file
    __objects (dic): dictionary - empty but will store all objects

    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns private class attribute object """
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = f"{type(obj).__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path) """
        serialized_obj = {}
        for key, value in self.__objects.items():
            serialized_obj[key] = value.to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(serialized_obj, f)

    def reload(self):
        """Deserializes JSON file to __objects."""
        try:
            with open(self.__file_path, 'r') as file:
                data = json.load(file)
                for o in data.values():
                    clss_name = o['__class__']
                    del o['__class__']
                    self.new(eval(clss_name)(**o))
        except FileNotFoundError:
            pass
