#!/usr/bin/env python

from sys import argv

def greetings(name):
    """ Greets the user """
    print("Hello " + name + "!")

# one more extra argument after the script, user's name
if len(argv) == 2:
    greetings(name = argv[1])

# no additional arguments after script
else:
    print ("Hello World!")
