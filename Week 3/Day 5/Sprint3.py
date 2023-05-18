import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','#','$','%','&','(',')','*','+']



print("Welcome to the PyPassword Generator")
password_length = int(input("How long would you like your password to be?\n"))
password = ""

amount_letters = 0
amount_symbols = 0
amount_numbers = 0

while (amount_letters + amount_numbers + amount_symbols) != password_length:
    amount_letters = random.randint(1, password_length)
    amount_symbols = random.randint(1, password_length)
    amount_numbers = random.randint(1, password_length)

while len(password) != password_length:
    for i in range(amount_letters):
        password +=  letters[random.randint(0, amount_letters)]
    for j in range(amount_numbers):
        password +=  numbers[random.randint(0, amount_numbers)]
    for k in range(amount_symbols):
        password +=  symbols[random.randint(0, amount_symbols)]
        #Suffle the password
    if len(password) > password_length:
        break 
    password = list(password)
    random.shuffle(password)
    password = "".join(password)

print(str(password))
    