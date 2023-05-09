
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


class User:

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def make_withdraw(self, amount):
        self.account.withdraw(amount)
        return self
    
    def display_user_balance(self):
        self.account.display_account_info()
        print(self.account.balance)
        return self

user1 = User("Wyatt", "wyatthelmick@gmail.com")

user2 = User("Notwyatt", "notwyatt@gmail.com")

# user1.display_user_balance()
# user2.make_deposit(4000).make_withdraw(500).make_deposit(8000).display_user_balance()