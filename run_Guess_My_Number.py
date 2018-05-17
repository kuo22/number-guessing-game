import random
import math

def getRandomInt(a, b):
    return random.randint(a, b)

def isPrimeUnder1000(m):
    if (m > 1000 or m < 2):
        return False
    for i in range(2, math.ceil((math.sqrt(m)))):
        if (m % i == 0):
            return False
    return True

def is_n_minus_k_divisible_by_m(n, k, m):
    return ((n - k) % m == 0)

def phaseOne():
    option = int(input("1: Guess "))
    switcher = {
        1: guess
    }
    switcher.get(option, lambda: print("Invalid option"))()

def phaseTwo():
    return 2

def guess():
    guess = input("what is your guess? ")
    if (guess == secret_num):
        print("You got it!")
        playing = False
    else:
        print("That is wrong")

playing = True
score = 0
turns = 0
secret_num = getRandomInt(0, 1000)
print(secret_num)
while playing:
    phaseOne()


#num = input("Enter a number: ")
#print(isPrimeUnder1000(int(num)))
