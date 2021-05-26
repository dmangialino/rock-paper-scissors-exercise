# game.py

print("Welcome to Rock, Paper, Scissors, Shoot!")

# Prompt user to enter a chocice, i.e., rock, paper, or scissors
user_choice = input("Please choose one of 'rock', 'paper', 'scissors': ")
print("USER CHOICE:", user_choice)


# Validate that the user inputted a valid choice (i.e., rock, paper, or scissors)
# If the input is valid, will continue with the rest of the program
# If selection is invalid, will notify user of invalid input and exit the program
if (user_choice == "rock") or (user_choice == "paper") or (user_choice == "scissors"):
    print("VALID CHOICE! KEEP GOING")
else:
    print("Oops! Invalid input. Please re-run the program to try again.")
    exit()



print("This is the end of our game. Please play again!")