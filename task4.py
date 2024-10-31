#! python3
#
# Surface area of a cone
# Find the surface area of a cone given the height and the radius.
# You will need to ask the user to enter in both variables, and will 
# need to use the Pythagorean relationship to find the slant height. 
# (2 points)
#
# Inputs:
# height, radius
#
# Outputs:
# surface area
#
# Test output
# r = 3
# h = 5
# sa = 83.2297607912
import math

r=input("height:")
#convert to a number
r = float(r)
h=input("radius")
#covert to a number
h = float(h)
A= (3.141592653589793*r)*(r+math.pow(h,2)+math.pow(r,2))*(0.5)
Output=(A)
print(A)