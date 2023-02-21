#!/usr/bin/python3
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
        pass

    
    def help_quit(self):
        """ help for quit """
        print("Quit command to exit the program\n")


if __name__ == '__main__':
    HBNBCommand().cmdloop()