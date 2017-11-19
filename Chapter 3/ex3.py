#Write a program that determines the molecular weight of a hydrocarbon based on the number of hydrogen,
#carbon, and oxygen atoms.
#CnH2n+2

import cmath

def molecularweight():
    carbon = 12.011
    hydrogen = 1.0079

    carbon_weight = carbon;
    hydrogen_weight = (2 * hydrogen) + 2;

    molecular_weight = carbon_weight + hydrogen_weight;

    print("The molecular weight of hydrocarbon is ", molecular_weight)


molecularweight()