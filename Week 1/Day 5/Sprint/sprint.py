# Banking application capable of making withdrawls and deposits
# Use a file
# Add error handleing e.g. letters, or withdrawing more than allowed
# Document that contains your money is called Bank Data.txt
# Transactions file that holds the logs for wihdrawls and deposits is called Transaction Log.txt
# Show user balance before asking if they would like to withdraw or deposit then show the new balance after the transaction
# If invalid data is provided the should be text that displays to call it invalid


import os, re
import art

directory = os.path.dirname(os.path.realpath(__file__))
print(directory)
file_location = os.path.join(directory,"Bank Data.txt")

def readfile(file_location):#READS THE CONTENTS OF A FILE
    with open(file_location, 'r') as f:
        contents = f.read()
        print(contents)

def clearfile(file_location):#CLEARS THE CONTENTS OF A FILE
    open(file_location, 'w').close()

def replace_text(file_location, replacing, replacer):#REPLACES TEXT IN A FILE
    f = open(file_location, 'r+')
    data = f.read()
    f.seek(0)
    f.write(re.sub(replacing, replacer, data)) #Replaces the specific character or text in the first input
    f.truncate()

def errorhandling(value):
    try:
        value = int(value)
        return True
    except:
        try:
            value = float(value)
            return True
        except:
            print('You did not enter a valid number!!!')
            return False

def deposits(value, file_location):
    f = open(file_location,'r+')
    current_balance = f.read()
    print(f'Your balance was R{current_balance}')
    current_balance = float(current_balance)
    current_balance += float(value)
    f = open(file_location, 'w')
    f.write(str(current_balance))
    print(f'Your balance was R{current_balance}')
    f.close()
'''
Ask the user how much they would like to withdraw
Set a variable equal to that value
Open the textfile containing the user details in read mode
Set a variable equal to the value inside the textfile
Display there current balance 
Set the current balance equal to current balance minus the withdraw amount
Display the withdraw amomunt
Display the new balance
Open the textfile in write mode
Write the current balance to the textfile
Close the textfile
'''
def withdrawls(value, file_location):
    f = open(file_location,'r+')
    current_balance = f.read()
    print(f'Your balance was R{current_balance}')
    current_balance = float(current_balance)
    current_balance -= float(value)
    if current_balance < 0:
        print('Dam son slow down, you broke!!!')
    else:
        print('Keep it going my boy.')
    f = open(file_location, 'w')
    f.write(str(current_balance))
    print(f'Your balance changed to R{current_balance}')
    f.close()

print(art.a)

try:
    # Tries to access file
    f = open(file_location, 'a')
except:
    # If file cant be accessed it created a new file
    f = open(file_location, 'x')
    # Check the different format you can open with, creating the document in write mode, need to write directly to the document after creation
    f.write('0')
    f.close()
options = input('What would you like to do? Type 1 for Withdrawls, 2 for Deposits and 3 for Transaction history: ')
try:
    if int(options) == 1:
        amount = input('Enter the amount you would like to withdraw: R')
        if errorhandling(amount):
            withdrawls(amount, file_location)
    elif int(options) == 2:
        amount = input('Enter the amount you would like to deposit: R')
        if errorhandling(amount):
            deposits(amount, file_location)
    elif int(options) == 3:
        pass
    else:
        print('You did not pick a valid option.')
except:
     print('You did not enter a valid input.')
