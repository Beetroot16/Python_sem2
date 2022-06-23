import random
from cryptography.fernet import Fernet
from rsa import encrypt

names = []
types = []
accountnos = []
balance = []
passwords = []


class account:
    def __init__(self,name,account_number,account_type,password):
        self.name = name
        self.account_number = account_number
        self.account_type = account_type
        self.password = password

class savings:
    def __init__(self,balance,rate,time):
        self.balance = balance
        self.rate = rate
        self.time = time

class current:
    def __init__(self,balance):
        self.balance = balance

def password():
    account.password = input("Set your account password: ")
    checker = input("Re-type your password: ")
    if checker == account.password:
        key = Fernet.generate_key()
        fernet = Fernet(key)
        encrypted = fernet.encrypt(account.password.encode())
        passwords.append(encrypted)
        decoded = fernet.decrypt(encrypted).decode()
        print(decoded)
    else:
        print("Passwords don't match !")
        password()

def add_user():
    account.name = input("Enter your name: ")
    names.append(account.name)
    password()
    account.account_number = random.randint(1000000,9999999)
    accountnos.append(account.account_number)
    account.account_type = input("Enter your account type: ").lower()
    types.append(account.account_type)

    if account.account_type == "savings":
        savings.balance = int(input("Deposit cash: "))
        balance.append(savings.balance)
    elif account.account_type == "current":
        current.balance = int(input("Deposit cash: "))
        balance.append(current.balance)

    print("Thank you for choosing our bank !")

def search():
    global names
    search = input("Enter your name: ")
    index = names.index(search)
    return index

def access():
    index = search()
    print(names[index] + "'s " + types[index] +" account")
    if types[index] == "savings":
        print("Your account balance is:",balance[index])
    elif types[index] == "current":
        print("Your account balance is:",balance[index])
        if balance[index] <= 500:
            print("Your account balance is below 500 , a 2% penalty will be charged")
            balance[index] = balance[index] - 0.2*(balance[index])
            print("Your new account balance is:",balance[index])

def deposite():
    index = search()
    print(names[index] + "'s " + types[index] +" account")
    deposite = int(input("Enter the ammount you want to deposit: "))
    if types[index] == "savings":
        balance[index] = balance[index] + deposite
        print("Your new account balance is:",balance[index])
    elif types[index] == "current":
        balance[index] = balance[index] + deposite
        print("Your new account balance is:",balance[index])

def withdraw():
    index = search()
    print(names[index] + "'s " + types[index] +" account")
    withdraw = int(input("Enter the ammount you want to withdraw: "))
    if types[index] == "savings":
        if withdraw < balance[index]:
            balance[index] = balance[index] - withdraw
            print("Your new account balance is:",balance[index])
        else:
            print("Insufficient balance")
            print("Your account balance is:",balance[index])
    elif types[index] == "current":
        if withdraw < balance[index]:
            balance[index] = balance[index] - withdraw
            if balance[index] <= 500:
                print("Your account balance is below 500 , a 2% penalty will be charged")
                balance[index] = balance[index] - 0.2*(balance[index])
            print("Your new account balance is:",balance[index])
        else:
            print("Insufficient balance")
            print("Your account balance is:",balance[index])

def calculate():
    index = search()
    print(names[index] + "'s " + types[index] +" account")
    if types[index] == "savings":
        rate = int(input("Enter the rate of interest in percent: "))
        time = int(input("Enter the time of the investment in years: "))

        balance[index] = balance[index] + ((balance[index]*rate*time)/100)
        print("You recieved a total interest of",(balance[index]*rate*time)/100)
        print("Your new account balance is:",balance[index])
    else:
        print("This is not a savings account.")

def transfer():
    index = search()
    print(names[index] + "'s " + types[index] +" account")
    reciever = input("Enter the recievers name: ")
    index2 = names.index(reciever)
    ammount = int(input("Enter the ammount you want to tranfer: "))
    if ammount < balance[index]:
        balance[index] = balance[index] - ammount
        balance[index2] = balance[index2] + ammount
    else:
        print("Insufficient balance")
        print("Your account balance is:",balance[index])

    print(str(names[index]) + "'s balance " + str(balance[index]))
    print(str(names[index2]) + "'s balance " + str(balance[index2]))
    
def admin():
    password = input("Enter the password: ")
    if password == "abcd":
        print(names)
        print(types)
        print(accountnos)
        print(balance)

print("""WELCOME TO THE BANK !
Press 1 to create an account
Press 2 to access your account
Press 3 to deposite money in your account
Press 4 to withdraw money from your account
Press 5 to calculate intrest in savings account
Press 6 to transfer
Press 7 to access admin
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
    if t ==6:
        transfer()
    if t ==7:
        admin()