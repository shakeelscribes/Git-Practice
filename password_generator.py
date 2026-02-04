# Update Branch Changes

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to PyPassword Generator!")

n_letters = int(input("Enter the Count of letters:\n"))
n_numbers = int(input("Enter the Count of Numbers:\n"))
n_symbols = int(input("Enter the Count of Symbols:\n"))

l_letters = []
l_numbers = []
l_symbols = []


for i in range(n_letters):
    i = random.choice(letters)
    l_letters += i


for i in range(n_numbers):
    i = random.choice(numbers)
    l_numbers += i


for i in range(n_symbols):
    i = random.choice(symbols)
    l_symbols += i


joindd = l_letters + l_numbers + l_symbols
print(joindd)
divyaprasad = len(joindd)
rand_password = []
random.shuffle(joindd)

for j in joindd:
    password = j
    rand_password.append(password)
print(rand_password)

final_pass = ''.join(rand_password)
print(f"The Pasword is {final_pass}")