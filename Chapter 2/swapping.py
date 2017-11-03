def test():

    num1 = eval(input("Enter a number "))
    num2 = eval(input("Enter second number "))

    temp = num1
    num1 = num2
    num2 = temp

    print("After swapping, num2 value is" ,num2)

test();
