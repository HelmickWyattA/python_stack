class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
user1 = User("Wyatt", "Helmick", "wyatthelmick@gmai.com", "25")

def display_info(self):
    print("=")
    print(f"First Name: {self.first_name}")
    print(f"Last Name: {self.last_name}")
    print(f"Age: {self.age}")
    print(f"Rewards Member?: {self.is_rewards_member}")
    print(f"Rewards Points: {self.gold_card_points}")


user1.display_info()


