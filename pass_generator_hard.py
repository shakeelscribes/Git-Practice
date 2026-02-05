import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("*" * 100)
print("                                   Welcome to PyPassword Generator!")
print("*" * 100)



n_letters = int(input("Enter the Count of Letters: "))
n_numbers = int(input("Enter the Count of Numbers: "))
n_symbols = int(input("Enter the Count of Symbools: "))

ab = []
bc =[]
cd =[]
for l in range(n_letters):
    r_letters = random.choice(letters)
    ab += r_letters

for l in range(n_numbers):
    r_numbers = random.choice(numbers)
    bc += r_numbers

for l in range(n_symbols):
    r_symbols = random.choice(symbols)
    cd += r_symbols

rand_pass = ab + bc + cd
random.shuffle(rand_pass)
password = ""

for r in rand_pass:
    password += r
print(f"The Password is: {password}")

