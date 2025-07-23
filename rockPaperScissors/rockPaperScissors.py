import random

print("Welcome to Rock, Paper, Scissors!")

# Get user input
user_choice = input("Enter rock, paper, or scissors: ")
user_choice = user_choice.lower()

# Keep asking until they enter a valid choice
while user_choice != "rock" and user_choice != "paper" and user_choice != "scissors":
    print("That's not a valid choice!")
    user_choice = input("Please enter rock, paper, or scissors: ")
    user_choice = user_choice.lower()

# Computer picks randomly
computer_choice = random.choice(["rock", "paper", "scissors"])

# Tell the user what they picked
print("You picked:", user_choice)
print("Computer picked:", computer_choice)

# Figure out who wins
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