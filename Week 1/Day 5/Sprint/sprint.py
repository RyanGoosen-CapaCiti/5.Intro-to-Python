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
    current_balance = float(current_balance)
    current_balance += float(value)
    f = open(file_location, 'w')
    f.write(str(current_balance))
    f.close()

def withdrawls(value, file_location):
    f = open(file_location,'r+')
    current_balance = f.read()
    current_balance = float(current_balance)
    current_balance -= float(value)
    f = open(file_location, 'w')
    f.write(str(current_balance))
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

amount = input('Enter the amount you would like to deposit: ')
readfile(file_location)
errorhandling(amount)
deposits(amount, file_location)
readfile(file_location)
f.close()

