#!/usr/bin/env python

# import regular expressions
import re

while True:
    first_line = input("Enter a number (or a letter to exit): ")
    # if the given characters do not consist numbers (negative numbers!)
    if not re.match("^[0-9;-;+]*$", first_line):
        exit()
    else:
        second_line = input("Enter an operation: ")
        third_line = int(input("Enter another number: "))
        if second_line == "+":
            print("Result: ", int(first_line) + third_line)
        elif second_line == "-":
                print("Result: ", int(first_line) - third_line)
        elif second_line == "*":
            print("Result: ", int(first_line) * third_line)
        elif second_line == "/":
            print("Result: ", int(first_line) / third_line)
        print("")
