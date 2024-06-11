class user:
    def __init__(self,first_name,last_name,email,age,is_rewards_member = False,gold_card_points = 0):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = is_rewards_member
        self.gold_card_points = gold_card_points

    def display_info(self):
        print(f"first name : {self.first_name}")
        print(f"last name : {self.last_name}")
        print(f"email : {self.email}")
        print(f"age : {self.age}")
        print(f"is rewards member ? : {self.is_rewards_member}")
        print(f"points in gold card : {self.gold_card_points}")

    def enroll(self):
        if self.is_rewards_member:
            print("user already a member")
            return self
        self.is_rewards_member = True
        self.gold_card_points = 200

    def spend_points(self, amount):
        self.gold_card_points = self.gold_card_points - amount
        return self
        
anis = user("anis","ben selma","bs@gmail.com",40)
anis.display_info().enroll().spend_points(50)
Ahmed_youssef = user("Ahmed_youssef","ben selma","ay_bs@gmail.com",8)
Elaa = user("Elaa","ben selma","E_bs@gmail.com",5)
Ahmed_youssef.display_info().enroll().spend_points(80)
Elaa.display_info().enroll().spend_points(100)

