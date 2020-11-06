import random

class BankAccount:
    def __init__(self, full_name, balance):
        self.full_name = full_name
        self.account_number = random.randInt(10000000, 99999999)
        self.routing_number = 62738412
        self.balance = balance

    def deposit(self, amount):
        self.amount = amount

        balance += amount

        print(f"Amount Deposited: {amount}")


    