import random

# all letters to refer to
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# greeting
print("Welcome to the PyPassword Generator!")

# get input of no of letters
nr_letters= int(input("How many letters would you like in your password?\n")) 
# get input of no of symbols
nr_symbols = int(input(f"How many symbols would you like?\n"))
# get  input of no of numbers
nr_numbers = int(input(f"How many numbers would you like?\n"))

# a list where we save random letters, symbols and number in that order
password = []
for letter_nr in range(0, nr_letters):
  random_index = random.randint(0,len(letters)-1)
  password += letters[random_index]

for symbol_nr in range(0, nr_symbols):
  random_index = random.randint(0,len(symbols)-1)
  password += symbols[random_index]

for number_nr in range(0, nr_numbers):
  random_index = random.randint(0,len(numbers)-1)
  password += numbers[random_index]

# shuffling items in list to have shuffled order of letter, symbols and numbers and converting it to a string
f_password = ""
for letters in range(0, len(password)-1):
  random_index = random.randint(0,len(password)-1)
  f_password += password[random_index]

# printing final password
print(f_password)
