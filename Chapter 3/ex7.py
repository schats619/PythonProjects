import cmath

def distanceTwoPoints():
    y1 = int(input("Enter a value for y1: "));
    y2 = int(input("Enter a value for y2: "));
    x1 = int(input("Enter a value for x1: "));
    x2 = int(input("Enter a value for x2: "));

    square1 = (y2 - y1) ^ 2
    square2 = (x2 - x1) ^ 2

    distance = cmath.sqrt(square1 - square2);

    print("The distance of the 2 points is : ", distance)

distanceTwoPoints()
