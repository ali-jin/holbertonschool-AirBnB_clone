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


if __name__ == '__main__':
    HBNBCommand().cmdloop()