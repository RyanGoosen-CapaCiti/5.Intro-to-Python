import os
from datetime import datetime
import tkinter as tk
from tkinter import font, ttk, messagebox, simpledialog, scrolledtext
from PIL import Image, ImageTk

def opening_window():
    global window, file_location_BankLog, file_location_Accounts,file_location_Transactions, username

    # File Declarations
    directory = os.path.dirname(os.path.realpath(__file__))
    file_location_BankLog = os.path.join(directory,"Bank_Log.txt")
    file_location_Accounts = directory+'/Accounts/'
    file_location_Transactions = directory+'/Transaction History/'

    # Create GUI window
    window = tk.Tk()
    window.title("Banking Program")
    window.geometry('600x400+700+200')

    # Create title label and center it
    title = tk.Label(window, text="Welcome to P.I.M.P. BANK.")
    title_font = font.Font(family="Times New Roman", size=20, weight="bold")
    title['font'] = title_font
    title.pack(pady=20)

    # Image
    image_path = f"{directory}/Images/MicrosoftTeams-image-removebg-preview.png"  # Replace with the actual image file path
    image = Image.open(image_path)
    resized_image = image.resize((250, 250), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(resized_image)
    image_label = tk.Label(window, image=photo)
    x_pos = 180
    y_pos = 60
    image_label.place(x=x_pos, y=y_pos)

    # Create buttons
    button_login = ttk.Button(window, text="Login", width=15, style="Rounded.TButton", command=lambda: log_reg_window(1))
    button_login.pack(anchor='s',side=tk.LEFT, padx=10, pady=10)

    button_register = ttk.Button(window, text="Register", width=15, style="Rounded.TButton", command=lambda: log_reg_window(2))
    button_register.pack(anchor='s',side=tk.RIGHT, padx=10, pady=10)

    # Create custom style for rounded buttons
    style = ttk.Style()
    style.configure("Rounded.TButton", borderwidth=0, focuscolor="none", bordercolor="none", background="#444444", foreground="white", relief=tk.RAISED, font=("Arial", 12, "bold"), padding=10)
    style.map("Rounded.TButton", background=[("pressed", "#666666"), ("active", "#666666")])

    # Run the GUI window
    window.mainloop()

def log_reg_window(button_id):
    global username_entry, pin_entry, new_window

    window.destroy()  # Close the original window
    new_window = tk.Tk()
    username_text = 'USERNAME:'
    pin_text = 'PIN:'
    if button_id == 1:
        new_window.title("Login")
        new_window.geometry('300x150+850+300')

        # Add login button
        login_button = ttk.Button(new_window, text="Login", command=user_exists, style="Rounded.TButton")
        login_button.pack(anchor='s', side=tk.LEFT, padx=5, pady=5)

        # Add close button
        close_button = ttk.Button(new_window, text="Close", command=new_window.destroy, style="Rounded.TButton")
        close_button.pack(anchor='s', side=tk.RIGHT, padx=5, pady=5)

    elif button_id == 2:
        new_window.title("Register")
        new_window.geometry('300x150+850+300')

        # Add register button
        register_button = ttk.Button(new_window, text="Register", command=register, style="Rounded.TButton")
        register_button.pack(anchor='s', side=tk.LEFT, padx=5, pady=5)

        # Add close button
        close_button = ttk.Button(new_window, text="Close", command=new_window.destroy, style="Rounded.TButton")
        close_button.pack(anchor='s', side=tk.RIGHT, padx=5, pady=5)

    # Add input fields for username and pin
    # Username
    username_label = tk.Label(new_window, text="USERNAME:")
    username_label.pack(pady=5)
    username_entry = tk.Entry(new_window)
    username_entry.pack()

    # Pin
    pin_label = tk.Label(new_window, text="PIN:")
    pin_label.pack()
    pin_entry = tk.Entry(new_window, show="*")  # Show asterisks for PIN
    pin_entry.pack()

    style = ttk.Style()
    style.configure("Rounded.TButton", borderwidth=0, focuscolor="none", bordercolor="none", background="#444444", foreground="white", relief=tk.RAISED, font=("Arial", 12, "bold"), padding=5)
    style.map("Rounded.TButton", background=[("pressed", "#666666"), ("active", "#666666")])


# LOGIN CODE
def user_exists():
    username = username_entry.get()
    pin = pin_entry.get()
    f = open(file_location_BankLog, 'r')
    document = f.readlines()
    fail = True
    for i in document: # In use check
        if username.lower() == i.split(' ')[0].lower():
            login(username,pin)
            fail = False
    if fail:
        messagebox.showerror('','Your username or pin is incorrect.')

def login(username, pin):
    login = f'{username.lower()} {pin}\n'
    f = open(file_location_BankLog, 'r')
    found = False
    # Checks if the login appears in the file
    # Return a value depending on if the account was found or not
    for i in f.readlines():
        if login == i:
            messagebox.showinfo('',f'WELCOME BACK {username.upper()}')
            new_window.destroy()
            main_function(username)
            found = True
    if not found:
        messagebox.showerror('','User not found.')


# REGISTRATION CODE
def register():
    username = username_entry.get()
    pin = pin_entry.get()

    if username_valid(username) and  pin_valid(pin):
        messagebox.showinfo('','Welcome new member')
        create_user_account(username, pin)
        new_window.destroy()
        main_function(username)

def create_user_account(username, pin): 
    login = username + ' ' + pin + '\n'
    # Add the user to Bank Log
    f = open(file_location_BankLog, 'a')
    f.write(login.lower())
    f.close()
    # Creating the users account which holds their balance
    f = open(f'{file_location_Accounts}{username.lower()}.txt', 'a')
    f.write('0')
    # Creating the users account which holds their transaction history
    f = open(f'{file_location_Transactions}{username.lower()}.txt', 'a')
    f.write("{:<12} {:<10} {:<8} {:<20}".format(
            'Date', 'Time','Amount', 'Transaction'
        ))

def pin_valid(pin):
    if len(pin) == 4: # Length check
        if pin.isnumeric(): # Number check 
            result = messagebox.askokcancel("Confirmation", f'Your pin is {pin}, Do you want to proceed?')# Conformation
            if result:
                return True
            else:
                messagebox.showerror('','Please try again.')
                return False
        else:
            messagebox.showerror('','Your pin can only be numbers.')
            return False
    else:
        messagebox.showerror('','The pin needs to be 4 numbers.')
        return False

def username_valid(username):
    # Change to include number but it must be just letters or (letters and nums)
    f = open(file_location_BankLog, 'r')
    document = f.readlines()
    available = True
    if username.isalpha(): # String check
        if (len(username) >= 4) and (len(username) <= 12): # Length check
            for i in document: # In use check
                if username.lower() == i.split(' ')[0].lower():
                    available = False
                    messagebox.showerror('','That username is taken')
                    return available
            if available:
                return available
            else:
                messagebox.showerror('','That username is taken')
                available = False
                return available
        else:
            messagebox.showerror('','The username you have entered needs to be a min of 4 and a max 12 characters.') 
            available = False
            return available
    else:
        messagebox.showerror('','The username can only be letters.')
        available = False
        return available

def balance_check(username):
    global balance
    # Simple functioin which just prints the users account balance
    f = open(f'{file_location_Accounts}{username}.txt', 'r')
    balance = f.read()
    


def main_function(username):
    global balance, main_window
    
    main_window = tk.Tk()
    main_window.title('')
    main_window.geometry('600x180+700+200')

    # Add a label for current balance
    balance_check(username)
    balance_label = tk.Label(main_window, text=f"Current Balance:\tR{balance}")
    balance_label.grid(row=0, column=0, sticky='w', pady=10)

    # Add a label for action prompt
    action_label = tk.Label(main_window, text="What would you like to do?")
    action_label.grid(row=1, column=0, columnspan=3, pady=10)

    # Define dark grey color
    dark_grey = "#444444"

    # Add buttons
    withdraw_button = tk.Button(main_window, text="WITHDRAW",  background=dark_grey, foreground="white", command=lambda: withdraw(username))
    withdraw_button.grid(row=2, column=0, padx=(10, 5), pady=10, sticky='w')

    deposit_button = tk.Button(main_window, text="DEPOSIT",  background=dark_grey, foreground="white", command=lambda:deposit(username))
    deposit_button.grid(row=2, column=1, padx=(5, 5), pady=10)

    th_button = tk.Button(main_window, text="TRANSACTION HISTORY",  background=dark_grey, foreground="white", command=lambda:see_history(username))
    th_button.grid(row=2, column=2, padx=(5, 10), pady=10, sticky='e')

    # Add a close button that stretches across the window
    close_button = tk.Button(main_window, text="Close", command=main_window.destroy, background=dark_grey, foreground="white")
    close_button.grid(row=3, column=0, columnspan=3, sticky='we', padx=10, pady=10)

    # Configure column weights to stretch buttons horizontally
    main_window.grid_columnconfigure(0, weight=1)
    main_window.grid_columnconfigure(1, weight=1)
    main_window.grid_columnconfigure(2, weight=1)



def deposit(username):
    amount = simpledialog.askstring("Input", "Enter a value:R")
    if amount.isnumeric():
        amount = int(amount)
        # Open the users account file using their username as the search function
        # Opens the file in read mode
        f = open(f'{file_location_Accounts}{username}.txt', 'r')
        # Reads the current balance of the account and sets it to a variable
        balance = int(f.read())
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
        make_history(username, amount, 'deposits')
        main_window.destroy()
        main_function(username)
    else:
        print('Please only enter numbers.')
    
def withdraw(username):
    global balance
    amount = simpledialog.askstring("Input", "Enter a value:R")
    if amount.isnumeric():
        amount = int(amount)
        # Open the users account file using their username as the search function
        # Opens the file in read mode
        f = open(f'{file_location_Accounts}{username}.txt', 'r')
        # Reads the current balance of the account and sets it to a variable
        balance = int(f.read())
        if balance >= amount:
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
            make_history(username, amount, 'withdrawl')
            main_window.destroy()
            main_function(username)
        else:
            messagebox.showerror('','You do not have a sufficient balance for this request.')
    else:
        messagebox.showerror('','Please only enter numbers.')
    

def make_history(username, amount, transaction):
    current_datetime = datetime.now()
    current_date = current_datetime.date()
    current_time = current_datetime.strftime("%H:%M:%S")
    # Open the file in append mode and write the formatted data
    with open(f"{file_location_Transactions}{username}.txt", "a") as f:
        f.write('\n')
        f.write("{:<12} {:<10} {:<8} {:<20}".format(
            str(current_date), current_time, str(amount), transaction
        ))

def see_history(username):
    window = tk.Tk()
    window.title("Text File Viewer")
    text_area = scrolledtext.ScrolledText(window, width=80, height=30)
    text_area.pack(padx=10, pady=10)
    
    with open(f"{file_location_Transactions}{username}.txt", "r") as f:
        lines = f.readlines()

    for line in lines:
        text_area.insert(tk.END, line)

opening_window()


'''
I want to welcome you all to our second round of funding for our banking app,
We are techloyalties and I am Mr Goosen,

We will be going through all the new edits we made since our last presentation
Being a GUI, classes, a nifty password genera6tor and
'''