# Import module
import random

# Define variables
Odds = 1 # <--- It's easier to think of odds and even as 1 and 2
Even = 2 # <--- There's probably an easier way than this but hell if I know 

# Create the cho han function with parameters for the guess and bet
def cho_han(guess, bet):
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    total = die1 + die2
    print(total) # <--- Checking the actual number and displaying it
    if guess == 2 and total % 2 == 0: # <--- If the total has a remainder it's checked against the 0
        print("Even. You win! You won {} dollars.".format(bet))
    elif guess == 2 and total % 2 != 0:
        print("Odds. You lose! You lost {} dollars.".format(bet))
    elif guess == 1 and total % 2 == 0:
        print("Even. You lose! You lost {} dollars.".format(bet))
    else:
        print("Odds. You win! You won {} dollars.".format(bet))


# Call the function to run the program
cho_han(Even, 15) # <--- The user's guess and bet go here

### NOTES ###
# As with the coin flip function, I wanted this to be user input based but alas
# Still need to modify the code to be scalable with running total, user input, more checks, etc.
