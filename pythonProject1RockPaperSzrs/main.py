#Lab 3 - Rock Paper Scissors
#Chris Cooper
import random
print('Hello, welcome to a game of Rock Paper Scissors Lizard Spock')
print('For instuctions please look up basic rock paper scissors tutorial')
options = ("rock", "paper", "scissors", "lizard", "spock")
player = None
player2 = random.choice(options)
player = input("Enter your throw (rock, paper, scissors, lizard, spock):\n")
if player == player2:
    print("It looks like its a tie!")
elif player == "rock" and player2 == "scissors":
    print("You won!")
elif player == "paper" and player2 == "rock":
    print("You won!")
elif player == "scissors" and player2 == "paper":
    print("You won!")
elif player == "lizard" and player2 == "paper":
    print("You won!")
elif player == "lizard" and player2 == "spock":
    print("You won!")
else:
    print("You lose!")