#!/usr/bin/python3
"""
    Program that contains the entry point of the command interpreter :
    the HBnB Console .
"""
import cmd
import sys


class HBNBCommand(cmd.Cmd):
    """
    Class HBNBCommand: command interpreter
    """

    prompt = "(hbnb) "

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

    
    def do_create(self, args):
        """
        Creates a new instance of BaseModel, saves it (to the JSON file),
        and prints the id
        """
        args = args.split()[0]

        if not args:
            print("** class name missing **")

        elif args in self.tab:
            new_instance = eval(args + '()')
            new_instance.save()

            print(new_instance.id)
    
        else:
            print("** class doesn't exist **")
    
    def do_show(self, args):
        """
        Prints the string representation of an instance based on
        the class name and id
        """
        args = args.split()

        if not args:
            print("** class name missing **")
        


    def do_destroy(self, args):
        """
        Deletes an instance based on the class name and id
        """

    def do_all(self, args):
        """
        Prints all string representation of all instances based or not
        on the class name
        """


    def do_update(self, args):
        """
        Updates an instance based on the class name and id by adding or
        updating attribute (save the change into the JSON file)
        """

if __name__ == '__main__':
    HBNBCommand().cmdloop()