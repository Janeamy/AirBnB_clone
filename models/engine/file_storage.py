#!/usr/bin/python3

import json

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as f:
            to_save = {}
            for key, value in FileStorage.__objects.items():
                to_save[key] = value.to_dict()
            json.dump(to_save, f)

    def reload(self):
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as f:
                FileStorage.__objects = json.load(f)
        except FileNotFoundError:
            pass
