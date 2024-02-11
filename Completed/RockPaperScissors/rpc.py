
import random
while True:
    choices = ["rock","paper","scissors"]
    computer = random.choice(choices)
    player = None
    while player not in choices:
        player = input("Choose one of the following: Rock, Paper, Scissors").lower()

    if player == computer:
        print("Player has chosen:", player)
        print("Computer has chosen:", computer)
        print("Tie Game")

    elif player == "rock":
        if computer == "scissors":
            print("Player has chosen:", player)
            print("Computer has chosen:", computer)
            print("Rock beats Scissors , Player Wins")
        if computer == "paper":
            print("Player has chosen:", player)
            print("Computer has chosen:", computer)
            print("Paper beats rock , PC Wins")

    elif player == "paper":
        if computer == "scissors":
            print("Player has chosen:", player)
            print("Computer has chosen:", computer)
            print("Scissors beats Paper , PC Wins")
        if computer == "rock":
            print("Player has chosen:", player)
            print("Computer has chosen:", computer)
            print("Paper beats rock , Player Wins")

    elif player == "scissors":
        if computer == "paper":
            print("Player has chosen:", player)
            print("Computer has chosen:", computer)
            print("Scissors beats Paper , Player Wins")
        if computer == "rock":
            print("Player has chosen:", player)
            print("Computer has chosen:", computer)
            print("Rock beats Scissors , PC Wins")

    play_again = input("Would you like to play again? (yes/no)").lower()
    if play_again != "yes":
        break
print("Good Bye")
