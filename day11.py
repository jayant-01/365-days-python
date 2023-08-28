# generating a password

import random

print("Welcome to the password generator!")

size = int(input("How many characters would you like your password to be? "))
password = ""
s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
for i in range(size):
    password += random.choice(s)
print(password)