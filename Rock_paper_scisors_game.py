import random
import time

# print("Welcome to Abeds Rock, Paper, Scissors Game!")
# time.sleep(1)
# print("You will be playing against the computer.")
# time.sleep(1)
# print("You can choose Rock, Paper, or Scissors.")
# time.sleep(1)
# print("The computer will randomly choose one of the three options.")
# time.sleep(1)
# print("The winner is determined by the following rules:")
# print("Rock beats Scissors")
# print("Scissors beats Paper")
# print("Paper beats Rock")
# time.sleep(1)
# print("Let's start the game!")
# time.sleep(1)
# print("Enter your choice (rock, paper, scissors):")
# client_choice = input().lower()
# if client_choice not in ["rock", "paper", "scissors"]:
#     print("Invalid choice. Please choose rock, paper, or scissors.")
# else:
#     print("You chose:", client_choice)
#     time.sleep(1)
#     print("The computer is making its choice...")
#     time.sleep(2)
#     computer_choice = random.choice(["rock", "paper", "scissors"])
#     print("The computer chose:", computer_choice)
#     time.sleep(1)

#     if client_choice == computer_choice:
#         print("It's a tie!")
#     elif (client_choice == "rock" and computer_choice == "scissors") or \
#          (client_choice == "scissors" and computer_choice == "paper") or \
#          (client_choice == "paper" and computer_choice == "rock"):
#         print("You win!")
#     else:
#         print("You lose!")
#     time.sleep(1)




class Player:
    def __init__(self, choices):
        self.choices = choices

def check_winner(first_player_pick, second_player_pick):
    if first_player_pick == second_player_pick:
        return "Tie"
    elif (first_player_pick == "rock" and second_player_pick == "scissors") or \
         (first_player_pick == "scissors" and second_player_pick == "paper") or \
         (first_player_pick == "paper" and second_player_pick == "rock"):
        return 1  # First player wins
    else:
        return 0  # Second player wins

def play_game(abed, ahmad):
    count_abed = 0
    count_ahmad = 0
    for i in range(len(abed.choices)):  # Loop through the choices
        result = check_winner(abed.choices[i], ahmad.choices[i])
        if result == 1:
            count_abed += 1
        elif result == 0:
            count_ahmad += 1

    if count_abed > count_ahmad:
        print("you Win!")
    elif count_ahmad > count_abed:
        print("Computer wins!")
    else:
        print("It's a tie!")

def main():
    picks = input("Enter your list of choices (rock, paper, scissors) separated by spaces: ").split()
    abed = Player(picks)
    ahmad = Player([random.choice(["rock", "paper", "scissors"]) for _ in picks])
    play_game(abed, ahmad)

if __name__ == "__main__":
    main()
