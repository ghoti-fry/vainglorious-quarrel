# Import module
import random

# Create a list of all the numbered cards in a deck (36 cards)
deck_of_cards = [
    2, 3, 4, 5, 6, 7, 8, 9, 10,
    2, 3, 4, 5, 6, 7, 8, 9, 10,
    2, 3, 4, 5, 6, 7, 8, 9, 10,
    2, 3, 4, 5, 6, 7, 8, 9, 10
    ]

# Make two variables, one for each player
player1_card = random.sample(deck_of_cards, k = 1)
player2_card = random.sample(deck_of_cards, k = 1)

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

# Call the function, set player1_bet in first parameter, then player2_bet
higher_card(15, 20)
