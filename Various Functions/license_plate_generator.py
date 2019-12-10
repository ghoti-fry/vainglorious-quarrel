# Import necessary modules
import random
import sys
import time

# Create two tuples containing the letters and numbers
# Lists could be used but since the values will never change, 
# tuples work better
letters = ("A", "B", "C", "D", "E", 
            "F", "G", "H", "I", "J", 
            "K", "L", "M", "N", "O", 
            "P", "Q", "R", "S", "T", 
            "U", "V", "W", "X", "Y", "Z")

numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

# Create two variables that generate 3 random letters and numbers 
# from the tuples respectively
three_letters = random.choices(letters, k = 3)
three_numbers = random.choices(numbers, k = 3)

# This function is uneccesary for the final function to perform, 
# but I just think it makes the program look nicer
def print_slow(str):
	for letter in str:
		sys.stdout.write(letter)
		sys.stdout.flush()
		time.sleep(0.025)
		
# The main function of the program. 
# Takes the previous variables and organizes them into a readable format.
def license_generator(three_letters, three_numbers):
	print_slow("### Random SC License Plate Generator ###\n\n")
	time.sleep(0.5)
	print_slow("Your random plate is:\n\n" + str(three_letters) + " - " 
                    + str(three_numbers))
	
# Finally we call the final function and our program is complete
license_generator(three_letters, three_numbers)
