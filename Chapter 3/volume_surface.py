def volarea():
    pie = 3.14
    x = eval(input("Enter radius : "))
    volume = 4/3 * pie * (x * x * x)
    area = 4 * pie * (x * x)

    print("The volume is ", volume)
    print("The area is ", area)

volarea()