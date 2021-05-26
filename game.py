# Load random module for use in simulating computer selection in the game
import random

player = "Player One"
print("---------------------")
print("Welcome '", player, "' to Rock, Paper, Scissors, Shoot!")
print("---------------------")

# Prompt user to enter a chocice, i.e., rock, paper, or scissors and store it in
# ...user_choice variable
user_choice = input("Please choose one of 'rock', 'paper', 'scissors': ")
print("You chose:", user_choice)


# Validate that the user inputted a valid choice (i.e., rock, paper, or scissors)
# ...if the input is valid, will continue with the rest of the program
# ...if selection is invalid, will notify user of invalid input and exit the program
if (user_choice == "rock") or (user_choice == "paper") or (user_choice == "scissors"):
    print("---------------------")
else:
    print("Oops! Invalid input. Please re-run the program to try again.")
    exit()


# Simulate computer selection to play against user

# Create list with valid options to provide to random.choice function
valid_options = ["rock", "paper", "scissors"]

# Pass valid_options list to random.choice function to simulate computer selection and 
# ...store it in computer_choice variable
computer_choice = random.choice(valid_options)
print("The computer chose:", computer_choice)
print("---------------------")


# Determine the winner between user and computer choices
# Rock beats scissors, paper beats rock, scissors beat paper, same choice results in tie
if user_choice == computer_choice:
    print("It's a tie!")
elif user_choice == "rock":
    if (computer_choice == "paper"):
        print("Computer wins!", computer_choice, "beats", user_choice)
    elif (computer_choice == "scissors"):
        print("You win!", user_choice, "beats", computer_choice)
elif user_choice == "paper":
    if (computer_choice == "scissors"):
        print("Computer wins!", computer_choice, "beats", user_choice)
    elif (computer_choice == "rock"):
        print("You win!", user_choice, "beats", computer_choice)
elif user_choice == "scissors":
    if (computer_choice == "rock"):
        print("Computer wins!", computer_choice, "beats", user_choice)
    elif (computer_choice == "paper"):
        print("You win!", user_choice, "beats", computer_choice)
else:
    print("Oops! There was an error. Please try again.")

print("---------------------")
print("Thanks for playing! Please play again!")