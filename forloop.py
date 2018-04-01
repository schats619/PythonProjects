import cmath

def condition():
    age = int((input("Enter your age")))

    if age < 30:
        print("You are born in Mumbai")
    elif age > 30:
        print("You are born in Bangalore")


def looping():
    food = ['bacon', 'tuna', 'ham', 'cheese']

    for f in food:
        print(f);
        print(len(f))

condition()
looping()