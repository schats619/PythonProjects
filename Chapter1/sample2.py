# def main():
#     print("Hello, World!")
#     print("Hello", "World!")
#     print(3)
#     print(3.0)
#     print(2+3)
#     print(2.0 + 3.0)
#     print("2" + "3")
#     print("2 + 3 = ", 2 + 3)
#     print(2 * 3)
#
# main()


def calculate():


    print("Example of a chaotic function sample 2");
    n = eval(input("How many numbers should I print"))
    x = eval(input("Enter a number from 0:1 "))
    for i in range(n):
        x = 2.0 * x * (1 - x)

        print(x)
calculate()



