# Program: Bank Account class
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Amount positive honi chahiye")
            return
        self.balance += amount
        print(f"{amount} jama hue. Balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Balance kaafi nahi hai")
            return
        self.balance -= amount
        print(f"{amount} nikaale. Balance: {self.balance}")


acc = BankAccount("Jamshaid", 1000)
acc.deposit(500)
acc.withdraw(300)
acc.withdraw(5000)
