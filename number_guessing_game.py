import random
import math

playing = True
playerQuit = False
score = 0
turns = 0

# Returns a random number between a and b, inclusive.
def getRandomInt(a, b):
    return random.randint(a, b)

# Returns true if m is a prime number under 1000, false otherwise.
def is_prime_under_1000(m):
    if (m > 1000 or m < 2):
        return False
    
    # Primality test
    for i in range(2, math.ceil((math.sqrt(m)))):
        if (m % i == 0):
            return False
    return True

# Returns true if n subtracted by k, divided by m is divisible.
def is_n_minus_k_divisible_by_m(n, k, m):
    return ((n - k) % m == 0)

# Asks the user to pick between ask, guess, and quit.
def choose_option():
    option = int(input("1: Ask\n2: Guess\n3: Quit\nPick an option: "))
    switcher = {
        1: ask,
        2: guess,
        3: quit
    }
    switcher.get(option, lambda: print("Invalid option"))()

# Let user input a number to subtract from the secret number and a prime number to divide from the result.
def ask():
    global secret_num
    print("Pick a number n to subtract from secret number, then a prime number to divide the result. I will tell you if the division was divisible.")
    subtract = int(input("Subtract from secret number: "))
    divide = int(input("What to divide after subtracting: "))
    print("divide is a prime: ", is_prime_under_1000(divide))
    if 0 > subtract > divide:
        print("n needs to be between 0 and the divisor.")
    elif not is_prime_under_1000(divide):
        print("divisor needs to be a prime number under 1000")
    elif is_n_minus_k_divisible_by_m(secret_num, subtract, divide):
        print("The result is divisible.")
    else:
        print("The result is not divisible.")

# Let the user input an integer to guess the secret number and adds an extra turn for the player.
def guess():
    global turns
    turns += 1
    guess = int(input("what is your guess? "))
    if (guess == secret_num):
        print("You got it!")
        global playing
        playing = False
    else:
        print("That is wrong")

# Quit the current game.
def quit():
    global playing
    global playerQuit
    playing = False
    playerQuit = True

# Returns a score of 0 if the user quits the game, or a score that is the secret number divided by the number of guesses taken.
def get_Score(secret_num, turns, quit):
    if quit:
        return 0
    else:
        return secret_num / turns

# Runs the game.
def run_guess_my_number():
    while playing:
        choose_option()  
    print("Final score: ", get_Score(secret_num, turns, playerQuit))

secret_num = getRandomInt(0, 1000)

if __name__ == '__main__':
    run_guess_my_number()