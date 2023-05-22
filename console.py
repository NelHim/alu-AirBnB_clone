#!/usr/bin/python3
"""Entry point of the command interpreter"""

import cmd
import models
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '  # Set the custom prompt

    def do_quit(self, arg):
        """Exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program on EOF (Ctrl+D)"""
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass

    def do_create(self, arg):
        """Create a new instance and print its ID"""
        if not arg:
            print("** class name missing **")
        elif arg not in models.classes:
            print("** class doesn't exist **")
        else:
            new_instance = models.classes[arg]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """Print the string representation of an instance"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in models.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            if key not in models.storage.all():
                print("** no instance found **")
            else:
                print(models.storage.all()[key])

    def do_destroy(self, arg):
        """Delete an instance based on the class name and id"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in models.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            if key not in models.storage.all():
                print("** no instance found **")
            else:
                del models.storage.all()[key]
                models.storage.save()

    def do_all(self, arg):
        """Print the string representations of all instances"""
        args = arg.split()

        if not arg:
            print([str(value) for value in models.storage.all().values()])
        elif args[0] not in models.classes:
            print("** class doesn't exist **")
        else:
            print([str(value) for key, value in models.storage.all().items()
                   if key.split('.')[0] == args[0]])

    def do_update(self, arg):
        """Update an instance based on the class name and id"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in models.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            key = args[0] + "." + args[1]
            if key not in models.storage.all():
                print("** no instance found **")
            else:
                setattr(models.storage.all()[key], args[2], args[3])
                models.storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()