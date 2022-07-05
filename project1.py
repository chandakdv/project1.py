1--------

from math import pi
r = float(input ("enter radius of the circle : "))
calculateArea = str(pi * r**2);
print (" area of circle of radius" + str(r) + " is: " + calculateArea)



2--------

fn= input("Enter Filename: ")

f = fn.split(".")

print ("Extension of the file is : " + f[-1])
