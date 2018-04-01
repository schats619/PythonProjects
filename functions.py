# def age(myage):
#     newage = myage/2 + 7
#     return newage
#
# the_age = age(27)
# print("Sourav is " ,the_age, "years old")
#
#
#
# def grade(marks):
#     if marks >= 90:
#         print("You got A ")
#     elif marks >=80:
#         print("You got B ")
#     else:
#         print("Fail!")
#
#
# grade(80)

def status(visa='Unknown'):
    if visa is 'f1':
        visa = "Student"
    elif visa is 'h1B':
        visa = "Worker"


    print(visa)

status('f1')
status('h1B')
status()

l=[]
for i in range (2000,3200):
    if (i%7==0) and (i%5!=0):
        l.append(str(i))

print (', '.join(l))

def name(name='Sourav', action='ate', item='fruits' ):
    print(name,action,item)

name(item='banana', action='ate')