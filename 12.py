#Write a program to sum a series of numbers entered by user.
#The program should first prompt the user for how many numbers
#are to be summed. It should then input each of the numbers and print a total sum.

import cmath

def sum():
    num = int(input("Enter a value"))
    x = range(1, num+1)
    print(list(x) + 1)
sum()


