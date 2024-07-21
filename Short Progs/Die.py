# Write a random number generator that generates random numbers between 1 and 6 (simulates a dice).

def Roll_Dice() :
    import random
    Face = random.randint(1,6)
    return Face

print(Roll_Dice())
