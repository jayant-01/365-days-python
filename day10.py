# dice roll simulation

import random
print("Welcome to the dice roll simulator!")

print("would you like to roll the dice?")

while True:
    answer = input("Y/N: ")
    if answer == "Y" or answer == "y":
        print("Rolling...")
        print(random.randint(1,6))
        print("would you like to roll the dice again?")
    elif answer == "N" or answer == "n":
        print("Goodbye!")
        break
    else:
        print("Invalid input")
        print("would you like to roll the dice again?")