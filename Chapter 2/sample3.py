#calculate the interest
def main():
    print("The program calculates the future value")
    print("of a 10-year investment")

    principal = eval(input("Enter the initial principal: "))
    inv = eval(input("Enter the annual initial rate: "))

    for i in range(10):
        principal = principal * (1 + inv)

    print("The value in 10 years is: " , principal)

main()