import random
import string

letters = string.ascii_letters
digits = string.digits
symbols = string.punctuation

all_characters = letters + digits + symbols

length = int(input("Enter password length: "))

password = ""
for i in range(length):
    password += random.choice(all_characters)

print("Your random password is:", password)