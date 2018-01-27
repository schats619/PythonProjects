#Area of the triangle

import cmath

def triangle():
    a = int(input("Enter the value for a: "))
    b = int(input("Enter the value for b: "))
    c = int(input("Enter the value for c: "))

    s = (a + b + c) / 2

    area = cmath.sqrt(s * (s - a) * (s - b) * (s - c))

    print("The value of s is : ", s)

    print("The area of the triangle is : ", area)

triangle()
