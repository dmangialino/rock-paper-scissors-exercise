# Load random module for use in simulating computer selection in the game
import random

print("Welcome to Rock, Paper, Scissors, Shoot!")

# Prompt user to enter a chocice, i.e., rock, paper, or scissors and store it in
# ...user_choice variable
user_choice = input("Please choose one of 'rock', 'paper', 'scissors': ")
print("USER CHOICE:", user_choice)


# Validate that the user inputted a valid choice (i.e., rock, paper, or scissors)
# ...if the input is valid, will continue with the rest of the program
# ...if selection is invalid, will notify user of invalid input and exit the program
if (user_choice == "rock") or (user_choice == "paper") or (user_choice == "scissors"):
    print("VALID CHOICE! KEEP GOING")
else:
    print("Oops! Invalid input. Please re-run the program to try again.")
    exit()


# Simulate computer selection to play against user

# Create list with valid options to provide to random.choice function
valid_options = ["rock", "paper", "scissors"]

# Pass valid_options list to random.choice function to simulate computer selection and 
# ...store it in computer_choice variable
computer_choice = random.choice(valid_options)
print("COMPUTER_CHOICE:", computer_choice)



print("This is the end of our game. Please play again!")