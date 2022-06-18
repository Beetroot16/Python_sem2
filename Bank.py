import random

class account:
    def __init__(self,name,account_number,account_type):
        self.name = name
        self.account_number = account_number
        self.account_type = account_type

class savings:
    def __init__(self,balance):
        self.balance = balance

class current:
    def __init__(self,balance,rate,time):
        self.balance = balance
        self.rate = rate
        self.time = time

def add_user():
    account.name = input("Enter your name: ")
    account.account_number = random.randint(1000000,9999999)
    account.account_type = input("Enter your account type: ").lower()

    if account.account_type == "savings":
        savings.balance = int(input("Deposit cash: "))
    elif account.account_type == "current":
        current.balance = int(input("Deposit cash: "))

    print("Thank you for choosing our bank !")

def access():
    print(account.name + "'s " + account.account_type +" account")
    if account.account_type == "savings":
        print("Your account balance is:",savings.balance)
    elif account.account_type == "current":
        print("Your account balance is:",current.balance)
        if current.balance <= 500:
            print("Your account balance is below 500 , a 2% penalty will be charged")
            current.balance = current.balance - 0.2*(current.balance)
            print("Your new account balance is:",current.balance)

def deposite():
    deposite = int(input("Enter the ammount you want to deposit: "))
    if account.account_type == "savings":
        savings.balance = savings.balance + deposite
        print("Your new account balance is:",savings.balance)
    elif account.account_type == "current":
        current.balance = current.balance + deposite
        print("Your new account balance is:",current.balance)

def withdraw():
    withdraw = int(input("Enter the ammount you want to withdraw: "))
    if account.account_type == "savings":
        if withdraw < savings.balance:
            savings.balance = savings.balance - withdraw
            print("Your new account balance is:",savings.balance)
        else:
            print("Insufficient balance")
            print("Your account balance is:",savings.balance)
    elif account.account_type == "current":
        if withdraw < current.balance:
            current.balance = current.balance - withdraw
            if current.balance <= 500:
                print("Your account balance is below 500 , a 2% penalty will be charged")
                current.balance = current.balance - 0.2*(current.balance)
            print("Your new account balance is:",current.balance)
        else:
            print("Insufficient balance")

def calculate():
    if account.account_type == "savings":
        rate = int(input("Enter the rate of interest in percent: "))
        time = int(input("Enter the time of the investment in years: "))

        savings.balance = savings.balance + (savings.balance*rate*time)
        print("You recieved a total interest of",(savings.balance*rate*time))
        print("Your new account balance is:",savings.balance)
    else:
        print("This is not a savings account.")

print("""WELCOME TO THE BANK !
Press 1 to create an account
Press 2 to access your account
Press 3 to deposite money in your account
Press 4 to withdraw money from your account
Press 5 to calculate intrest in savings account
""")
while True:
    t = int(input(">> "))
    
    if t == 1:
        add_user()
    if t == 2:
        access()
    if t == 3:
        deposite()
    if t == 4:
        withdraw()
    if t == 5:
        calculate()