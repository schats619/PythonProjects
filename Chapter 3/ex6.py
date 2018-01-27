import cmath

def slopeline():

    y1 = int(input("Enter a value for y1: "))
    y2 = int(input("Enter a value for y2: "))
    x1 = int(input("Enter a value for x1: "))
    x2 = int(input("Enter a value for x2: "))

    slope_line = (y2 - y1) / (x2 - x1)


    print("The slope of a line is: ", slope_line)

slopeline()

