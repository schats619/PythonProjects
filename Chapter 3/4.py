def test1():
    for i in range(1,11):
        print(i*i)

def test2():
    for i in [1, 3, 5, 7, 9]:
        print(i, ":", i**3)
    print(i)

def test3():
    x=2
    y=10
    for j in range(0, y, x):
        print(j, end="")
        print(x+y)
    print("done")

def test4():
    ans=0
    for i in range(1, 11):
        ans=ans+i*i
        print(i)
    print(ans)

options = {0: test1,
           1: test2,
           2: test3,
           3: test4,
}

options[0]()
print("\n")
options[1]()
print("\n")
options[2]()
print("\n")
options[3]()