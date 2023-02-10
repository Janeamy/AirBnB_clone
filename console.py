#!/usr/bin/python3

import cmd

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def help_quit(self):
        print("Quit command to exit the program")

    def help_EOF(self):
        print("EOF command to exit the program")

    def emptyline(self):
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()

"""
Here is the updated version of the HBNBCommand class in console.py that implements the required commands:
"""

import cmd
import models
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """Command interpreter for HBNB"""
    prompt = "(hbnb) "
    
    def do_quit(self, line)
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """EOF command to exit the program"""
        return True

    def do_create(self, line):
        """Create a new instance of a class and save it to the JSON file"""
        if not line:
            print("** class name missing **")
        else:
            class_name = line.split()[0]
            if class_name in models.classes():
                new_model = eval(class_name + "()")
                new_model.save()
                print(new_model.id)
            else:
                print("** class doesn't exist **")

    def do_show(self, line):
        """Print the string representation of an instance based on the class name and id"""
        if not line:
            print("** class name missing **")
        else:
            class_name, instance_id = line.split()[0], line.split()[1] if len(line.split()) > 1 else None
            if class_name in models.classes():
                if instance_id:
                    key = "{}.{}".format(class_name, instance_id)
                    if key in models.all().keys():
                        print(models.all()[key])
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
    def do_destroy(self, line):
        """Delete an instance based on the class name and id"""
        if not line:
            print("** class name missing **")
        else:
            class_name, instance_id = line.split()[0], line.split()[1] if len(line.split()) > 1 else None
            if class_name in models.classes():
                if instance_id
                key = "{}.{}".format(class_name, instance_id)
                if key in models.all().keys():
                    models.all().pop(key)
                    models.save()
                else:
                    print("** no instance found **")
            else:
                print("** class doesn't exist **")

    def do_all(self, line):
        """Print all string representation of all instances based or not on the class name"""
        class_name = line.split()[0] if line else None
        if not class_name or class_name in models.classes():
            instances = [str(value) for key, value in models.all().items()
                    if not class_name or key.split(".")[0] == class_name]
            print(instances)
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        """Update an instance based on the class name

"""
Update your command interpreter (console.py) to allow show, create, destroy, update and all used with User.
""

import cmd
import models

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_create(self, arg):
        """Create a new instance of BaseModel, save it (to the JSON file) and print the id.
        Ex: $ create BaseModel"""
        if arg == "":
            print("** class name missing **")
        elif arg not in models.all_classes:
            print("** class doesn't exist **")
        else:
            new_instance = models.all_classes[arg]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class name and id.
        Ex: $ show BaseModel 1234-1234-1234."""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in models.all_classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            instance_id = args[1]
            instances = models.storage.all()
            if "{}.{}".format(args[0], instance_id) not in instances:
                print("** no instance found **")
            else:
                print(instances["{}.{}".format(args[0], instance_id)])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id (save the change into the JSON file).
        Ex: $ destroy BaseModel 1234-1234-1234."""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in models.all_classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            instance_id = args[1]
            instances = models.storage.all()
            instance_key = "{}.{}".format(args[0], instance_id)
            if instance_key not in instances:
                print("** no instance found **")
            else:
                del instances[instance_key]
                models.storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances based or not on the class name.
        Ex: $ all BaseModel or $ all."""
        instances = models.storage.all()
        if arg == "":
            print([str(v) for v in instances.values()])
        elif arg not in models.all_classes:
            print("** class doesn't exist **")
        else:
            print([str(v)

"""updated code for the console.py file:"""

# console.py
from models import storage
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

class HBNBCommand:
    """
    Contains the entry point of the command interpreter
    """
    classes = {"BaseModel": BaseModel, "User": User,
            "State": State, "City": City,
            "Amenity": Amenity, "Place": Place,
            "Review": Review}

    def do_create(self, class_name, *args):
        """
        Creates a new instance of class_name
        """
        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            new_instance = HBNBCommand.classes[class_name]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, class_name, id):
        """
        Prints the string representation of an instance based on the class name
        and id
        """
        key = class_name + "." + id
        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
        el

