import random

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

def single(choice, bet):
    spin = random.randint(0, 36)
    print("The ball lands on", spin)
    if spin == choice:
        winnings = bet * 35
        print("You won! You collect your winnings of {} dollars"
              .format(winnings))
    else:
        print("You lost. You lose {} dollars"
              .format(bet))


def even_odd(choice, bet):
    spin = random.randint(0, 36)
    print("The ball lands on", spin)
    if spin == 0:
        print("0 is neither odd nor even. You lost {} dollars"
              .format(bet))
    elif spin % 2 == 0:
        if choice == 2 and spin != 0:
            print("You win! You won {} dollars"
                  .format(bet))
        elif choice == 1 and spin != 0:
            print("You guessed wrong! You lose {} dollars"
                  .format(bet))
    elif spin % 2 != 0:
        if choice == 2:
            print("You guessed wrong! You lose {} dollars"
                  .format(bet))
        elif spin % 2 != 0 and choice == 1:
            print("You win! You won {} dollars"
                  .format(bet))


def red_black(choice, bet):
    spin = random.randint(0, 36)
    print("The ball lands on", spin)
    if spin == 0:
        print("0 is neither red nor black. You lost {} dollars"
              .format(bet))
    elif spin in red:
        if choice == red:
            print("{} is red. You win! You collect {} dollars"
                  .format(spin, bet))
        elif choice == black:
            print("{} is red. You lost! You lose {} dollars"
                  .format(spin, bet))
    elif spin in black:
        if choice == black:
            print("{} is black. You win! You collect {} dollars"
                  .format(spin, bet))
        elif choice == red:
            print("{} is black. You lost! You lose {} dollars"
                  .format(spin, bet))


def low_high(choice, bet):
    spin = random.randint(0, 36)
    print("The ball lands on", spin)
    if spin == 0:
        print("0 is neither high nor low. You lost {} dollars"
              .format(bet))
    elif spin in low:
        if choice == low:
            print("{} is low. You win! You collect {} dollars"
                  .format(spin, bet))
        elif choice == high:
            print("{} is low. You lost! You lose {} dollars"
                  .format(spin, bet))
    elif spin in high:
        if choice == high:
            print("{} is high. You win! You collect {} dollars"
                  .format(spin, bet))
        elif choice == low:
            print("{} is high. You lost! You lose {} dollars"
                  .format(spin, bet))

# Uncomment to play the game
# single(21, 1500)
# even_odd(odd, 600)
# red_black(red, 1000)
# low_high(high, 500)
