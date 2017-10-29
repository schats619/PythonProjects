def hello():
    print("Hello world")
    print("Welcome to python World");

hello()


def main():

    print("Example of a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    for i in range(10): # basic for loop to print the no of times the input will be displayed
        x = 3.9 * x * (1-x)
        print(x)


main()


