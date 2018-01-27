import cmath

def gregEpact():
    year = int(input("Enter a 4 digit year: "))
    easterData = year//100
    epact = (8 + (easterData//4) - easterData + ((8*easterData + 13)//25) + 11*(year%19)) % 30

    print("The year entered is : ", year)
    print("The value of the epact is: ", epact)

gregEpact()