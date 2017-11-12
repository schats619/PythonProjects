#write a program to calculate the volume and surface area of a sphere
#from its radius, given as input.

import cmath

def solution():
    val1 = 4
    val2 = 3

    value = eval(input("Enter a value for the radius"))

    vol = (val1/val2) * 3.14 * value**3
    area = val1 * 3.14 * value**2

    print("The volume is ", vol)
    print("The area is ", area)

solution()
