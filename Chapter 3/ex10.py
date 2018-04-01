import cmath

def lengthOfLadder():
    height = int(input("Enter the height of the ladder: "))
    angle = 90

    length = height / cmath.sin(angle)
    print("The total length is: ", length)

lengthOfLadder()


