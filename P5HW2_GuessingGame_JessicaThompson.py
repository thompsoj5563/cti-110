# Guessing Game
# April 8, 2018
# CTI 110 P5HW2
# Jessica Thompson

import random

number = random.randint(1, 100)

def main():

    guess = int(input("Enter an integer from 1 to 100: "))

    if number > guess:
        print ("Too low, try again.")
    elif number < guess:
        print ("Too high, try again.")
    elif number != guess:
        print ("Congratulations! You guessed it!")
    else:
        print ("Guess again")

main()
