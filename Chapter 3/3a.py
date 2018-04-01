def testrange():
    for i in range(5):
        print(i)

def testrange1():
    for i in range(3, 10):
        print(i)

def testrange2():
    for i in range(4,13,3):
        print(i)

options = {0: testrange,
            1: testrange1,
            2: testrange2,
}

options[2]()