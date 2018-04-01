#write a program to find the sum of first n natural numbers where the value
#of n is provided by the user.

import cmath

def userInput():
    nat_num = int((input("Enter a value")))
    nat_form = nat_num * (nat_num + 1)/2
    print("The sum of natural num is ", nat_form)

userInput()