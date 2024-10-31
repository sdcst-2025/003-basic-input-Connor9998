#! python3
import math
# Find the volume of a sphere.
# You will ask the user to enter the radius of the sphere.
# Calculate the Volume and then display the result to the user.
# You will need to import the math module in order to use math.pi

# Inputs:
# radius
#
# Outputs
# volume
#
# test output radius of 3 should give volume of 113.09733552923254

x=3.141592653589793238462643383279502884197
y=input("The Radius:")
#convert to a number
y= float(y)
L=math.pow(y,3)*x*4/3
print(L)