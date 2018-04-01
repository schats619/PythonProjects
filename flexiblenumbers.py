# def funcadd(*args):
#     total=0
#     for a in args:
#         total+= a
#     print(total)
#
# funcadd(3)
# funcadd(3, 4, 5)
# funcadd(3,4,5,200)
#



#
# def calculate(age, gpa, amount):
#     total = (100-age) + (gpa - 4.0) + (2000-amount)
#     print(total)
#
# my_data=[1,100,200]
#
# calculate(my_data[0], my_data[1], my_data[2])
# calculate(*my_data)


#
# def fact(x):
#     if x == 0:
#         return 1
#     return x*fact(x-1)
#
# print("Enter a number")
# x= int(input())
# print(fact(x))
#
# food = {'Sourav':'ate apple', 'Ashish':' ate banana', 'Jorge':' ate mango'}
#
# for k,v in food.items():
#     print(k+v)


n = int(input())
d = dict()
for i in range(1, n+1):
    d[i] = i*i

print (d)

