#! python3
import math
# Solve a two step algebra equation.
# Two steps equations are in the format ax + b = c
# You will ask the user to enter in all 3 variables: a, b and c
# You will need to display the solution for the equation

# inputs
# a, b, c
#
# outputs
# solution for x
#
# test case: 5, 1, 11 should give x = 2

a=input("Number.1:")
#convert to a number
a = float(a)
b=input("Number.2:")
#convert to a number
b = float(b)
c=input("Number.3:")
#convert to a number
c = float(c)

x=c-b*a
print(x)