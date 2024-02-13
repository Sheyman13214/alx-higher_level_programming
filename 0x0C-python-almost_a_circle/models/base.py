#!/usr/bin/python3
"""This module is for the first Base Class Model"""
import json
import csv


class Base():
    """This is the base class model
    with a counter for handeling ids

        Attributes:
            __nb_objects = counter for the ids
    """
    __nb_objects = 0

    # Built in Functions
    def __init__(self, id=None):
        """Initialization of Base Object
            Arguments:
                id: id for the object, if id is None then assign __nb_objects
        """
        if (id is not None):
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    # Static methods

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries."""
        if list_dictionaries is None:
            return "[]"
        return (json.dumps(list_dictionaries))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string."""
        if json_string is None:
            return ([])
        if type(json_string) is not str:
            raise TypeError("json_string must be a string")
        return json.loads(json_string)

    # Class methods

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file."""
        with open(f"{cls.__name__}.json", 'w+') as f:
            obj_list = []
            if list_objs is None:
                f.write(cls.to_json_string(obj_list))
            else:
                for item in list_objs:
                    obj_list.append(cls.to_dictionary(item))
                f.write(cls.to_json_string(obj_list))

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances."""
        list_of_instances = []
        try:
            with open(f"{cls.__name__}.json", 'r') as f:
                for ln in f:
                    inst = cls.from_json_string(ln)
                    for item in inst:
                        list_of_instances.append(cls.create(**item))
        except Exception as e:
            return []

        return list_of_instances

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set.
           Arguements:
               cls (Class Object): class to create
               dictionary (dict): dictionary of attributes.
        """
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy = cls(1)

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Writes a list of serialized objects to a file in csv format"""

        with open(f"{cls.__name__}.csv", 'w', newline='') as f:
            writer = csv.writer(f)

            for o in list_objs:
                if cls.__name__ == "Rectangle":
                    writer.writerow([o.id, o.width, o.height, o.x, o.y])
                if cls.__name__ == "Square":
                    writer.writerow([o.id, o.size, o.x, o.y])

    @classmethod
    def load_from_file_csv(cls):
        """Returns a list of instances based on a csv file"""
        list_objs = []

        with open(f"{cls.__name__}.csv", 'r', newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                if cls.__name__ == "Rectangle":
                    dictionary = {
                            "id": int(row[0]),
                            "width": int(row[1]),
                            "height": int(row[2]),
                            "x": int(row[3]),
                            "y": int(row[4])
                            }

                if cls.__name__ == "Square":
                    dictionary = {
                            "id": int(row[0]),
                            "size": int(row[1]),
                            "x": int(row[2]),
                            "y": int(row[3])
                            }

                instance = cls.create(**dictionary)
                list_objs.append(instance)
        return list_objs
