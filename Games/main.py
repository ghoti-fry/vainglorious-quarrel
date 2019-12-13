#   -*- coding: utf-8 -*-
#   GNU General Public License v3
#   Jack Shuford

# This is where I'm storing all the seperate gambling modules so they're in one place
# To actually play the different games (I use "play" lightly), see the bottom of this file
# If you're curious how it all works I've commented throughout explaining some code

# Import necessary module first
import random

### Coin Flip ###

# Define the variables
heads = 1
tails = 2

# Main coin flipping function. Simply chooses 1 or 2 which translates to heads and tails.
# An if statement cycles through all scenarios and prints the appropriate response
def coin_flip(guess, bet): # The user's guess and bet amount will go in here
    flip = random.randint(1, 2) # random.randint() chooses the number
    if flip == 1 and guess == 1: # Compare the random number to the user's guess
        print("Heads. You win! You won {} dollars.".format(bet)) # Prints out which the side and how much was won/lost
    elif flip == 2 and guess == 2:
        print("Tails. You win! You won {} dollars.".format(bet)) 
    elif flip == 1 and guess != 1:
        print("Heads. You lose! You lost {} dollars.".format(bet))
    else:
        print("Tails. You lose! You lost {} dollars.".format(bet)) # .format() allows the bet to be inserted
    
### Notes on Coin Flip ###
# I wanted to write this so that the user is prompted for the guess and bet,
# but codecademy has trouble with user input so the parameters have to be set manually in editor.
# I did at least try to make a working input version of this but that proved to be
# more difficult than I anticipated. So, this simple function is what I got.


### Cho-Han Game ###

# Define variables
odd = 1 # It's easier to think of odds and even as 1 and 2
even = 2

# Create the cho han function with parameters for the guess and bet
def cho_han(guess, bet):
    die1 = random.randint(1, 6) # random.randint picks more than two numbers too lol
    die2 = random.randint(1, 6)
    total = die1 + die2
    print(total) # Shows the user what was rolled
    if guess == 2 and total % 2 == 0: # If the roll has a remainder when divided by 2 it's checked against the 0
        print("Even. You win! You won {} dollars.".format(bet))
    elif guess == 2 and total % 2 != 0:
        print("Odds. You lose! You lost {} dollars.".format(bet))
    elif guess == 1 and total % 2 == 0:
        print("Even. You lose! You lost {} dollars.".format(bet))
    else:
        print("Odds. You win! You won {} dollars.".format(bet))

### Notes on Cho-Han ###
# Like the coin flip function, I wanted this to be user input based, despite codecademy, but alas I failed.


### Higher Card Draw ###

# Create a list of all the numbered cards in a deck not counting the ace (36 cards)
deck_of_cards = [
    2, 3, 4, 5, 6, 7, 8, 9, 10,
    2, 3, 4, 5, 6, 7, 8, 9, 10,
    2, 3, 4, 5, 6, 7, 8, 9, 10,
    2, 3, 4, 5, 6, 7, 8, 9, 10
    ]

# Make two variables, one for each player
player1_card = random.sample(deck_of_cards, k = 1) # I used random.sample here so that it doesn't pick the same card twice
player2_card = random.sample(deck_of_cards, k = 1) # The k variable sets how many items are pulled from the list

# Write the function that will compare the two player's cards and choose the winner
# If player_1 wins, return an appropriate message and award that bet
# If player_2 wins, return the same
# In the event of a tie, neither player wins and no money is awarded
def higher_card(player1_bet, player2_bet):
    print("Player 1 drew:", player1_card)
    print("Player 2 drew:", player2_card)
    if player1_card > player2_card:
        print("Player 1 drew the higher card and wins {} dollars!".format(player1_bet))
        print("Player 2 lost and loses {} dollars".format(player2_bet))
    elif player2_card > player1_card:
        print("Player 2 drew the higher card and wins {} dollars!".format(player2_bet))
        print("Player 1 lost and loses {} dollars".format(player1_bet))
    else:
        print("It's a tie! No one wins OR loses in a tie!")


### Roulette ###

# Define functions
odd = 1
even = 2
red = [1, 3, 5, 7, 9, 12, 14, 16, 18,
       19, 21, 23, 25, 27, 30, 32, 34, 36]

black = [2, 4, 6, 8, 10, 11, 13, 15,
         17, 20, 22, 24, 26, 28, 29,
         31, 33, 35]

low = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
       11, 12, 13, 14, 15, 16, 17, 18]

high = [19, 20, 21, 22, 23, 24, 25,
        26, 27, 28, 29, 30, 31, 32,
        33, 34, 35, 36]

# Creating the seperate functions for each kind of bet

def single(choice, bet):
    spin = random.randint(0, 36) # Since this is a French wheel, there is no 00 tile
    print("The ball lands on", spin)
    if spin == choice:
        winnings = bet * 35 # Odds are 35 to 1 against with this bet
        print("You won! You collect your winnings of {} dollars".format(winnings))
    else:
        print("You lost. You lose {} dollars".format(bet))


def even_odd(choice, bet):
    spin = random.randint(0, 36)
    print("The ball lands on", spin)
    if spin == 0: # Since 0 isn't an option, it's set to a loss
        print("0 is neither odd nor even. You lost {} dollars".format(bet))
    elif spin % 2 == 0: # Checking if the number is even or odd
        if choice == 2 and spin != 0:
            print("You win! You won {} dollars".format(bet))
        elif choice == 1 and spin != 0:
            print("You guessed wrong! You lose {} dollars".format(bet))
    elif spin % 2 != 0:
        if choice == 2:
            print("You guessed wrong! You lose {} dollars".format(bet))
        elif spin % 2 != 0 and choice == 1:
            print("You win! You won {} dollars".format(bet))


def red_black(choice, bet):
    spin = random.randint(0, 36)
    print("The ball lands on", spin)
    if spin == 0:
        print("0 is neither red nor black. You lost {} dollars".format(bet))
    elif spin in red: 
        if choice == red:
            print("{} is red. You win! You collect {} dollars".format(spin, bet))
        elif choice == black:
            print("{} is red. You lost! You lose {} dollars".format(spin, bet))
    elif spin in black:
        if choice == black:
            print("{} is black. You win! You collect {} dollars".format(spin, bet))
        elif choice == red:
            print("{} is black. You lost! You lose {} dollars".format(spin, bet))


def low_high(choice, bet):
    spin = random.randint(0, 36)
    print("The ball lands on", spin)
    if spin == 0:
        print("0 is neither high nor low. You lost {} dollars".format(bet))
    elif spin in low:
        if choice == low:
            print("{} is low. You win! You collect {} dollars".format(spin, bet))
        elif choice == high:
            print("{} is low. You lost! You lose {} dollars".format(spin, bet))
    elif spin in high:
        if choice == high:
            print("{} is high. You win! You collect {} dollars".format(spin, bet))
        elif choice == low:
            print("{} is high. You lost! You lose {} dollars".format(spin, bet))

############################################################################
#                        "PLAY" THE GAMES HERE!                            #
# Uncomment by removing the first hashtag for the game you want and type-  #
# in the choice and bet amount for the appropriate kind of bet and game.   #
# Example bets are already written, delete them to make your own.          #
#                                                                          #
#                              PLEASE NOTE:                                #
# Entries like "heads" or "black" are case sensitive and that no quotes    #
# are used!!!                                                              #
############################################################################

# Coin Flip #

#coin_flip(heads, 25) # <--- Enter "heads" or "tails" and the bet

# Cho-Han #

#cho_han(odd, 125) # <--- Enter "odd" or "even" and the bet

# Higher Card Draw #

#higher_card(18, 20) # <--- Enter Player 1 bet and then Player 2 bet

# Roulette (French wheel) #

# Single Bet #
#single(21, 1500) # <--- Enter 0-36 inclusive and the bet

# Even or Odd Bet #
#even_odd(odd, 600) # <--- Enter "even" or "odd" and the bet

# Red or Black Bet #
#red_black(red, 1000) # <--- Enter "red" or "black" and the bet

# Low or High Bet #
#low_high(high, 500) # <--- Enter "low" or "high" and the bet
