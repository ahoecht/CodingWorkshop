"""
Now that we have successfully built our first program, it's time to build our
first GAME!
This project takes you through the process of creating a fun little version of
Rock, Paper, Scissors!
"""
 
### IMPORTS ###
from random import randint

### INITAIL SETUP VARIABLES ###
# List of possible moves in the game
moves = ["rock","paper","scissors"]

# Variable to end the game
quit = False

### MAIN LOOP ###
print("Welcome to Rock, Paper, Scissors!\n")
while quit == False:
    # Computer selects a move at random
    computer = moves[randint(0,2)]

    # Prompt player for move
    player = input("Enter rock, paper, or scissors: ")

    # Check result of game
    if player == computer:
        print("It's a Tie!\n")
    elif player == "rock":
        if computer == "paper":
            print("You Lose! Paper beats Rock\n")
        else:
            print("You Win! Rock beats Scissors\n")
    elif player == "paper":
        if computer == "scissors":
            print("You Lose! Scissors beats Paper\n")
        else:
            print("You Win! Paper beats Rock\n")
    elif player == "scissors":
        if computer == "rock":
            print("You Lose! Rock beats Scissors\n")
        else:
            print("You Win! Scissors beats Paper\n")
    else:
        print("Invalid move! Please try again!\n")

    loop = input("Would you like to play again? [y/n] ")

    if loop == "n":
        quit = True
    else:
        print("GAME ON!!! \n")
