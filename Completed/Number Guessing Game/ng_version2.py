'''
Create a number guessing game that asks for what level that the user wants to be on.(1 - n).
The level entered would allow for the program to choose a RANDOM number for the user to guess.
If the user inputs anything that is not a positive number, the program will reprompt for a number, No errors are given.
If the user's number is lower than the guessed number, the program will return "Too small!" and reprompt.
If the user's number is greater than the guessed number, the program will return "Too large!" and reprompt.
If the user's number matchs the guessed number, the program will return "Just right!" and exit.
'''

import random
import sys

def main():
    lvl = lvl_chosen("Level: ")
    secret_num = random.randint(1, lvl+1)
    while True:
        num = usr_number("Guess: ")
        if num > secret_num:
            print("Too large!")
            continue
        elif num < secret_num:
            print("Too small!")
            continue
        else:
            break
    sys.exit("Just right!")

def lvl_chosen(level):
    while True:
        lvl = input(level)
        if lvl.isnumeric():
            return int(lvl)
        else:
            continue

def usr_number(guess):
    while True:
        num = input(guess)
        if num.isnumeric():
            return int(num)
        else:
            continue
main()
