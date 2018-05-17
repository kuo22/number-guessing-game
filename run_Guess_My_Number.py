import random
import math

def getRandomInt(a, b):
    return random.randint(a, b)

def isPrimeUnder1000(m):
    if (m > 1000 or m <= 0):
        return False
    for i in range(2, int(math.sqrt(m)) + 1):
        if (m % i == 0):
            return False
    return True

num = input("Enter a number: ")
print(isPrimeUnder1000(int(num)))


    
def phaseOne():
    return 1

def phaseTwo():
    return 2

