from random import choice
from string import ascii_letters, digits, punctuation

characters = ascii_letters + digits + punctuation
length = input("Length: ")
length = int(length)

password = ""

for _ in range(length):
    character = choice(characters)
    password = password + character

print(password)
#d
