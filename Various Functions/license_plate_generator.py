import random
import sys
import time

letters = ("A", "B", "C", "D", "E", 
            "F", "G", "H", "I", "J", 
            "K", "L", "M", "N", "O", 
            "P", "Q", "R", "S", "T", 
            "U", "V", "W", "X", "Y", "Z")

numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

three_letters = random.choices(letters, k = 3)
three_numbers = random.choices(numbers, k = 3)

def print_slow(str):
	for letter in str:
		sys.stdout.write(letter)
		sys.stdout.flush()
		time.sleep(0.025)

def license_generator(three_letters, three_numbers):
	print_slow("### Random SC License Plate Generator ###\n\n")
	time.sleep(0.5)
	print_slow("Your random plate is:\n\n" + str(three_letters) + " - " + str(three_numbers))
	
license_generator(three_letters, three_numbers)
