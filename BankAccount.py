import random

class BankAccount:
    def __init__(self, full_name, balance):
        self.full_name = full_name
        self.account_number = random.randint(10000000, 99999999)
        self.routing_number = 62738412
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Amount Deposited: ${amount}. Your current balance is ${self.balance}.")

    def withdraw(self, amount):
        self.balance -= amount
        print(f"Amount withdrawn: ${amount}. Your current balance is ${self.balance}.")

    def get_balance(self):
        print(f"Your current balance is: ${self.balance}.")

    def add_interest(self):
        interest += balance * 0.00083
    
    def print_receipt(self):
        print(f"""Name: {self.full_name}
        Account Number: {self.account_number}
        Routing Number: {self.routing_number}
        Balance: ${self.balance}
        """)

new_account = BankAccount("Alex Shearer", 500)

new_account.deposit(50)
new_account.withdraw(375)
new_account.print_receipt()
        


    