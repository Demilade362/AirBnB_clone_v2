#!/usr/bin/python3
import json


class FileStorage:
    __file_path = 'file.json'
    __objects = {}

    def all(self, obj=None):
        new_dict = {}
        if obj:
            dict = FileStorage.__objects
            for key in dict:
                cls = key.split('.')
                if cls[0] == obj.__name__:
                    new_dict[key] = self.__objects[key]
            return new_dict
        else:
            return FileStorage.__objects

    def new(self, obj):
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        if obj:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            del self.__objects[key]

    def close(self):
        self.reload()