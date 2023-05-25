# Using Tkinter
# User should be able to: Create an account
#                         Login
# Account Registration: Username
#                       Opening balance
#                       Pin Number
# Login: Needs to match username and pin number
# User functionality: View transaction details
#                     Balance inquiry
#                     Credit and Debit amount


import os

def create_user_account(username, pin, file_location_BankLog, file_location_Accounts, file_location_Transactions): 
    # Opens the bank account log file
    # The username and pin is then entered in the nextline of bank account log
    # Asks the user if they would like to make a deposit
    # If yes it goes to the deposit screen if no it goes to the main screen
    login = username + ' ' + pin + '\n'

    # Add the user to Bank Log
    f = open(file_location_BankLog, 'a')
    f.write(login)
    f.close()

    # Creating the users account which holds their balance
    f = open(f'{file_location_Accounts}{username}.txt', 'a')
    f.write('0')

    # Creating the users account which holds their transaction history
    f = open(f'{file_location_Transactions}{username}.txt', 'a')


def login(username, pin, file_location_BankLog): 
    # Searches the BankLog file and looks through line for line to find a line that matches the username and pin the user entered
    # If none is found it shows an error message else it show a succesful login message
    # After the successful login the user is show another screen allowing them to make edits
    # Login is case sensitive
    # After the error message the user will be promted to reenter the login
    login = username + ' ' + pin + '\n'
    f = open(file_location_BankLog, 'r')
    line = ''
    # Checks if the login appears in the file
    # Return a value depending on if the account was found or not
    if login in f.readlines(0):
        print('Login successful')
        return True
    else:
        print('User not found')
        return False    

def deposit(username, file_location_Accounts, amount):
    # Open the users account file using their username as the search function
    # Opens the file in read mode
    f = open(f'{file_location_Accounts}{username}.txt', 'r')
    # Reads the current balance of the account and sets it to a variable
    balance = int(f.read())
    # Show the user their old balance
    print(f'Your old balance was R{balance}')
    # Opens the file in read mode to clear the old balance
    f = open(f'{file_location_Accounts}{username}.txt', 'w')
    # Adds the deposited amount to the old balance
    balance += amount
    # Writes the new balance to the text file
    f.write(str(balance))
    # Opens the file and readmode to read the new balance from the text file
    f = open(f'{file_location_Accounts}{username}.txt', 'r')
    # Reads the current balance of the account and sets it to a variable
    balance = f.read()
    print(f'Your new balance is R' + str(balance))
    
def withdraw(username, file_location_Accounts, amount):
    # Open the users account file using their username as the search function
    # Opens the file in read mode
    f = open(f'{file_location_Accounts}{username}.txt', 'r')
    # Reads the current balance of the account and sets it to a variable
    balance = int(f.read())
    # Show the user their old balance
    print(f'Your old balance was R{balance}')
    # Opens the file in read mode to clear the old balance
    f = open(f'{file_location_Accounts}{username}.txt', 'w')
    # Removes the deposited amount to the old balance
    balance -= amount
    # Writes the new balance to the text file
    f.write(str(balance))
    # Opens the file and readmode to read the new balance from the text file
    f = open(f'{file_location_Accounts}{username}.txt', 'r')
    # Reads the current balance of the account and sets it to a variable
    balance = f.read()
    print(f'Your new balance is R' + str(balance))
    
def balance_check(username, file_location_Accounts):
    # Simple functioin which just prints the users account balance
    f = open(f'{file_location_Accounts}{username}.txt', 'r')
    balance = f.read()
    print(balance)

def pin_valid(pin):
    pass
    # Length cant be more than 4 numbers
    # Needs to be numbers
    # Can't be a float or string
    # Check if the user is fine with the pin


def username_valid(username, file_location_BankLog):
    # Username cannot be longer than 12 characters
    # Username cant be shorted than 4 charackters
    # Username cant already exist
    # Username needs to be letters
    # Username is not case sentisitive so it can be lower, upper or a combination
    f = open(file_location_BankLog, 'r')
    document = f.read()
    if username.isalpha():
        if (len(username) >= 4) and (len(username) <= 12):
            if username not in document:
                pass
            else:
                print('This username already exits')
        else:
            print('The username you have entered needs to be a min of 4 and a max 12 characters.') 
    else:
        print('The username you have entered is not valid')
        # String check
        # Length check
        # Letter check
        # username conversion to lowercase
        # check if already exits

def testing(file_location_BankLog, username):
    f = open(file_location_BankLog, 'r')
    document = f.readlines()
    available = True
    for i in document:
        if username == i.split(' ')[0].lower():
            available = False
            break
    if available:
        print('This username is avaialable.')
    else:
        print('This username already exists.')

    # if username not in document:
    #     print(f'{username} is valid')
    # else:
    #     print('This username already exits')

directory = os.path.dirname(os.path.realpath(__file__))
file_location_BankLog = os.path.join(directory,"Bank_Log.txt")
file_location_Accounts = directory+'/Accounts/'
file_location_Transactions = directory+'/Transaction History/'
username = 'zainap' 
pin = '6633'
testing(file_location_BankLog, username)