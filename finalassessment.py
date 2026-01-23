# 2 Bank Management system

class BankAccount:
    def __init__(self, name, account_number, balance=0):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Amount deposited successfully")
        else:
            print("Invalid amount")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print("Amount withdrawn successfully")
        else:
            print("Insufficient balance or invalid amount")

    def display(self):
        print("Account Holder:", self.name)
        print("Account Number:", self.account_number)
        print("Balance:", self.balance)


class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, name, account_number):
        if account_number not in self.accounts:
            self.accounts[account_number] = BankAccount(name, account_number)
            print("Account created successfully")
        else:
            print("Account already exists")

    def get_account(self, account_number):
        return self.accounts.get(account_number)


bank = Bank()

while True:
    print("\n1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Display Account")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter account holder name: ")
        acc_no = input("Enter account number: ")
        bank.create_account(name, acc_no)

    elif choice == "2":
        acc_no = input("Enter account number: ")
        account = bank.get_account(acc_no)
        if account:
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
        else:
            print("Account not found")

    elif choice == "3":
        acc_no = input("Enter account number: ")
        account = bank.get_account(acc_no)
        if account:
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)
        else:
            print("Account not found")

    elif choice == "4":
        acc_no = input("Enter account number: ")
        account = bank.get_account(acc_no)
        if account:
            account.display()
        else:
            print("Account not found")

    elif choice == "5":
        print("Thank you for using the bank system")
        break

    else:
        print("Invalid choice")
        
        
        
 # 3 Quiz Game
 
 

score = 0  

print("Welcome to the Quiz Game!\n")


answer = input("1. What is the capital of India?\n ")
if answer.lower() == "delhi":
    print("Correct!")
    score += 1
else:
    print("Wrong! Correct answer is Delhi")


answer = input("\n2. What is 5 + 3? \n ")
if answer == "8":
    print("Correct!")
    score += 1
else:
    print("Wrong! Correct answer is 8")


answer = input("\n3. Python is a programming language (yes/no)? \n")
if answer.lower() == "yes":
    print("Correct!")
    score += 1
else:
    print("Wrong! Correct answer is yes")


answer = input("\n4. Which keyword is used to define a function in Python? \n ")
if answer.lower() == "def":
    print("Correct!")
    score += 1
else:
    print("Wrong! Correct answer is def")


print("\nQuiz Finished!")
print("Your total score is:", score, "out of 4")
       