# ...
# for i in range(101):
#     if i % 4 is 0:
#         print(i)
# ...
num = 243
sum = 0
mod = 0
temp = num
while temp != 0:

    mod = temp % 10
    sum = mod + sum
    temp = temp / 10

print(sum)