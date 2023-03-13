import random

# create a list of options
options = ["rock", "paper", "scissors"]

# get user input
user_choice = input("Choose rock, paper, or scissors: ").lower()

# randomly select computer choice
computer_choice = random.choice(options)

# print computer's choice
print(f"Computer chooses {computer_choice}.")

# determine the winner
if user_choice == computer_choice:
    print("It's a tie!")
elif user_choice == "rock" and computer_choice == "scissors":
    print("You win!")
elif user_choice == "paper" and computer_choice == "rock":
    print("You win!")
elif user_choice == "scissors" and computer_choice == "paper":
    print("You win!")
else:
    print("Computer wins!")
