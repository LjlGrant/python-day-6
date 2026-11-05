# Escape Characters
print("Dear Class, I am so sad to say that this is our Last day of Python.")

# Absolute v.s. Relative Paths

# Modules and Libraries
from importlib.metadata import files
from io import FileIO
import random

random_int = random.randint(1,10)
print(random_int)

deck_of_cards = {"King of Spades", "8 of Hearts", "2 of Diamonds"}


import math 


answer = math.sqrt(64)
print(answer)




with open("demo.txt", "w") as life:
    file.write("file I/0 is soooooo fun!")



# Challenge 1: logger.py
# Write a program that asks the user for their name
# And then Adds it to a guest_list.txt file


name = input("What is your name? ")

with open("guest_list.txt", "a") as file:
    file.write(name + "\n")

print("Your name has been added to the guest list!")




# Challenge 2
# Create file called line_counter.py
# Copy and paste song lyrics into a lyrics.txt file
# Write a program that outputs the TOTAL number of lines
