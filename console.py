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
    classes = ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]

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

    def do_create(self, arg = None):
        """
        Creates a new instance of BaseModel, saves it (to the JSON file),
        and prints the id
        """
        if arg == '':
            print ("** class name missing **")
        elif arg not in self.classes:
            print ("** class doesn't exist **")
        else:
            new = eval(arg)()
            new.save()
            print (new.id)

    def do_show(self, *args):
        """
        Prints the string representation of an instance based on the class name
        and id.
        """
        cmd = args[0].split()
        if args[0] == '':
            print ("** class name missing **")
        elif cmd[0] not in self.classes:
            print (f"** class doesn't exist **")
        elif len(cmd) <= 1:
            print ("** instance id missing **")
        else:
            key = cmd[0] + "." + cmd[1]
            try:
                dict = FileStorage.all(self)
                print (dict[key])
            except KeyError:
                print("** no instance found **")

    def do_destroy(self, *args):
        """
        Deletes an instance based on the class name and id
        """
        cmd = args[0].split()
        if args[0] == '':
            print ("** class name missing **")
        elif cmd[0] not in self.classes:
            print (f"** class doesn't exist **")
        elif len(cmd) <= 1:
            print ("** instance id missing **")
        else:
            key = cmd[0] + "." + cmd[1]
            try:
                dict = FileStorage.all(self)
                FileStorage.destroy(self, dict[key])
                FileStorage.save(self)
            except KeyError:
                print("** no instance found **")

    def do_all(self, arg = None):
        """
        Prints all string representation of all instances based or not
        on the class name
        """
        if arg != '' and arg not in self.classes:
            print ("** class doesn't exist **")
        else:
            try:
                dict = FileStorage.all(self)
                for key in dict:
                    if arg == '' or key.split(".")[0] == arg:
                        print (dict[key])
            except KeyError:
                print("** no instance found **")

    def do_update(self, *args):
        """
        Updates an instance based on the class name and id by adding or
        updating attribute (save the change into the JSON file)
        """
        cmd = args[0].split()
        if len(cmd) <= 0 or cmd[0] == '':
            print ("** class name missing **")
        elif cmd[0] not in self.models:
            print (f"** class doesn't exist **")
        elif len(cmd) <= 1 or cmd[1] == '':
            print ("** instance id missing **")
        elif len(cmd) <= 2 or cmd[2] == '':
            print ("** attribute name missing **")
        elif len(cmd) <= 3 or cmd[3] == '':
            print ("** value missing **")
        else:
            key = cmd[0] + "." + cmd[1]
            try:
                user = FileStorage.all(self)[key]
                setattr(user, cmd[2], cmd[3])
                user.save()
            except KeyError:
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()