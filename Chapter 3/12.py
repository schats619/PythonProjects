import cmath
def sumOfCubes():
    n = int(input("Enter a natural number \n"))
    part_1 = n * (n+1)
    part_2 = 2
    div = part_1 / part_2
    formula = div ** 2

    print("The sum of", n, "natural numbers", formula)

sumOfCubes()


