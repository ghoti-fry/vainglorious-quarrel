# Import necessary module
import random

# Define some variables
money = 100
Heads = 1
Tails = 2

# Main coin flip function. Simply chooses 1 or 2 which translates to heads and tails.
# A simple if statement cycles through all possible outcomes and prints the appropriate response.
def coin_flip(guess, bet):
    flip = random.randint(1, 2)
    if flip == 1 and guess == 1:
        print("Heads. You win! You won {} dollars.".format(bet))
    elif flip == 2 and guess == 2:
        print("Tails. You win! You won {} dollars.".format(bet))
    elif flip == 1 and guess != 1:
        print("Heads. You lose! You lost {} dollars.".format(bet))
    else:
        print("Tails. You lose! You lost {} dollars.".format(bet))
    
# Finally call coin_flip() to run the program
coin_flip(Heads, 15) # <--- The user's guess and bet go here

### Notes ###
# I wanted to write this so that the user is prompted for the guess and bet,
#   but codecademy has trouble with user input so the parameters have to be set manually.
# I also tried to make a working input version of this but that proved to be
#   more difficult than I anticipated. So, this simple function is what I got.
# Lastly, a running count of the user's money would be ideal, rather than simply stating
#   the amount won or lost, but that also proved difficult. Baby steps, I guess.
