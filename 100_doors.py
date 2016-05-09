#!/usr/bin/env python

#version 1
y = [x * x for x in range (1,11)]
print("The following doors are open:", y)

#version 2
solution = []

for i in range (1,11):
    a = i * i
    solution.append(a)
print("The following doors are open:", solution)

#version 3
print("The following doors are open:", [x * x for x in range (1,11)])
