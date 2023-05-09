class BankAccount:

    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance


    def deposit(self, amount):
        self.balance += amount
        print(f"You have deposited {amount}")
        return self


    def withdraw(self, amount):
        if amount > self.balance:
            self.balance - 5
            print("Insufficient Funds")
        else:
            self.balance -= amount
            print(f"You have withdrawn {amount}")
        return self

    def display_account_info(self):
        print(f"Your current account balance is {self.balance}")
        return self

    def yield_interest(self):
        print(self.int_rate)

account1 = BankAccount(10, 0.04)

account2 = BankAccount(200, 0.08)


account1.deposit(10).deposit(5).deposit(10).withdraw(15).display_account_info().yield_interest()
account2.deposit(500).withdraw(100).withdraw(10).withdraw(50).withdraw(20)
