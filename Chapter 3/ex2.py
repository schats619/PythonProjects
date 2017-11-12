#Write a program that calculates the cost per square inch of a circular
#given its diameter and price.
import cmath

def area_per_square():
    diameter = eval(input("Enter the diameter of the pizza \n "))
    price = eval(input("Enter the price of the pizza \n "))

    radius = diameter/2

    area = 3.14*radius**2
    print("The area is ", area)

    price_per_square_inch = price / area;

    print("The price per square inch pizza is ", price_per_square_inch)

area_per_square()