### Password generator using Python

import random
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["/", "@", "!", "#", "$", "%", "&", "*"]

print("welcome to password generator")

no_of_letters = int(input("How many letters you want = \n"))
no_of_numbers = int(input("How many numbers you want = \n"))
no_of_symbols = int(input("How many symbols you want = \n"))

password_list = []

for char in range(1, no_of_letters + 1):
    random_letters = random.choice(letters)
    password_list += random_letters
    
    
for char in range(1, no_of_numbers + 1):
    random_numbers = random.choice(numbers)
    password_list += random_numbers
    
    
for char in range(1, no_of_symbols + 1):
    random_symbols = random.choice(symbols)
    password_list += random_symbols

random.shuffle(password_list)

password = ""
for char in password_list:
    password += char
print(password)
