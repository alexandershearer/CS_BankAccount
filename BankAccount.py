import random

class BankAccount:
    #Set up the main function to get a name and balance
    def __init__(self, full_name, balance):
        self.full_name = full_name
        self.account_number = random.randint(10000000, 99999999)
        self.routing_number = 62738412
        self.balance = balance

    #Set up the function to make a deposit
    def deposit(self, amount):
        self.balance += amount
        print(f"Amount Deposited: ${amount}. Your current balance is ${self.balance}.")

    #Set up the function to make a withdraw
    def withdraw(self, amount):
        if self.balance - amount < 0 :
            self.balance -= 10
            print("Insufficient Funds. You will be charged an overdraft fee of $10")

        else:
            self.balance -= amount
            print(f"Amount withdrawn: ${amount}. Your current balance is ${self.balance}.")

    #Set up the function to check the current balance
    def get_balance(self):
        print(f"Your current balance is: ${self.balance}.")

    #Set up the function to add interest to the balance
    def add_interest(self):
        interest += self.balance * 0.00083
    
    #Set up the function to print out receipt for account
    def print_receipt(self):
        print(f"""
        Name: {self.full_name}
        Account Number: {self.account_number}
        Routing Number: {self.routing_number}
        Balance: ${self.balance}
        """)

#Make new account with name and balance
new_account = BankAccount("Alex Shearer", 500)

new_account.deposit(50)
new_account.withdraw(375)
new_account.print_receipt()
new_account.withdraw(142)

account2 = BankAccount("Jane Doe", 1000)

account2.deposit(100)
account2.withdraw(375)
account2.get_balance()

account2.print_receipt()
        


    