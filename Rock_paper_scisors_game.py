import random
import time

print("Welcome to Abeds Rock, Paper, Scissors Game!")
time.sleep(1)
print("You will be playing against the computer.")
time.sleep(1)
print("You can choose Rock, Paper, or Scissors.")
time.sleep(1)
print("The computer will randomly choose one of the three options.")
time.sleep(1)
print("The winner is determined by the following rules:")
print("Rock beats Scissors")
print("Scissors beats Paper")
print("Paper beats Rock")
time.sleep(1)
print("Let's start the game!")
time.sleep(1)
print("Enter your choice (rock, paper, scissors):")
client_choice = input().lower()
if client_choice not in ["rock", "paper", "scissors"]:
    print("Invalid choice. Please choose rock, paper, or scissors.")
else:
    print("You chose:", client_choice)
    time.sleep(1)
    print("The computer is making its choice...")
    time.sleep(2)
    computer_choice = random.choice(["rock", "paper", "scissors"])
    print("The computer chose:", computer_choice)
    time.sleep(1)

    if client_choice == computer_choice:
        print("It's a tie!")
    elif (client_choice == "rock" and computer_choice == "scissors") or \
         (client_choice == "scissors" and computer_choice == "paper") or \
         (client_choice == "paper" and computer_choice == "rock"):
        print("You win!")
    else:
        print("You lose!")
    time.sleep(1)