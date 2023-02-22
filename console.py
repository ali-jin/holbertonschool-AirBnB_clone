#!/usr/bin/python3
"""
    Program that contains the entry point of the command interpreter :
    the HBnB Console .
"""
import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import models


class HBNBCommand(cmd.Cmd):
    """
    Class HBNBCommand: command interpreter
    """

    prompt = "(hbnb) "
    file = None
    classes = (
        ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]
    )

    def do_quit(self, line):
        """ quit command to exit the program """
        return True

    def do_EOF(self, line):
        """ quit command to exit the program when EOF """
        return True

    def emptyline(self):
        """ Do nothing when an empty line is received """
        pass

    def help_quit(self):
        """ help for quit """
        print("Quit command to exit the program\n")

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, saves it (to the JSON file),
        and prints the id
        """
        if arg == '':
            print("** class name missing **")
        elif arg not in self.classes:
            print("** class doesn't exist **")
        else:
            new = eval(arg)()
            new.save()
            print(new.id)

    def do_show(self, args):
        """
        Prints the string representation of an instance based on the class name
        and id.
        """
        cmd = args.split()
        if not args:
            print("** class name missing **")
            """elif args[0] == '':
            print ("** class name missing **")"""
        elif cmd[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            if len(cmd) <= 1:
                print("** instance id missing **")
            else:
                key = cmd[0] + "." + cmd[1]

                if key not in models.storage.all().keys():
                    print("** no instance found **")
                else:
                    print(models.storage.all()[key])

    def do_destroy(self, args):
        """
        Deletes an instance based on the class name and id
        """
        cmd = args.split()
        if not args:
            print("** class name missing **")
            """elif args[0] == '':
            print ("** class name missing **")"""
        elif cmd[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            if len(cmd) <= 1:
                print("** instance id missing **")
            else:
                key = cmd[0] + "." + cmd[1]

                if key not in models.storage.all().keys():
                    print("** no instance found **")
                else:
                    del models.storage.all()[key]
                    models.storage.save()

    def do_all(self, arg):
        """
        Prints all string representation of all instances based or not
        on the class name
        """
        if arg and arg not in self.classes:
            print("** class doesn't exist **")
        elif not arg:
            print("{}".format(models.storage.all()))
        else:
            for key in models.storage.all().keys():
                if key[0] == arg[0]:
                    print(models.storage.all()[key])

    def do_update(self, args):
        """
        Updates an instance based on the class name and id by adding or
        updating attribute (save the change into the JSON file)
        """
        cmd = args.split()
        if not args:
            print("** class name missing **")
        elif cmd[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            if len(cmd) == 1:
                print("** instance id missing **")
            elif len(cmd) >= 2:
                key = cmd[0] + "." + cmd[1]

                if key not in models.storage.all().keys():
                    print("** no instance found **")
                elif len(cmd) == 2:
                    print("** attribute name missing **")
                elif len(cmd) == 3:
                    print("** value missing **")
                else:
                    setattr(models.storage.all()[key], cmd[2], cmd[3])


if __name__ == '__main__':
    HBNBCommand().cmdloop()
