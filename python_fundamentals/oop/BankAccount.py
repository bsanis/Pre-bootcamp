class bankaccount:
    accounts = []

    def __init__(self,int_rate,balance=0,interest=0.00):
        self.int_rate = int_rate
        self.balance = balance
        self.interest = interest
        bankaccount.accounts.append(self)
    
    def deposit(self,amount):
        self.balance = self.balance + amount
        return self

    def withdraw(self,amount):
        self.amount = self.balance - amount
        if self.amount < self.balance:
            self.balance = self.balance - amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance = self.balance - 5
            return self
    
    def display_account_info(self):
        print(f"balance : ${self.balance}")
        print(f"interest : ${self.interest}")
        return self

    def yield_interest(self):
        self.balance += self.balance * self.interest
        return self
    
    @classmethod
    def account_info(cls):
        for accounts in cls.accounts:
        accounts.display_account_info()

class user:
    def __init__(self,first_name,last_name,email,age,is_rewards_member = False,gold_card_points = 0):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = is_rewards_member
        self.gold_card_points = gold_card_points
        self.account = bankaccount(int_rate=0.02, balance=0)

anis_account = bankaccount(1925,120,0.02)
Elaa_account = bankaccount(2018,250,0.01)

anis_account.deposit(200).display_account_info().deposit(100).deposit(50).withdraw(85).display_account_info()
Elaa_account.deposit(120).deposit(75).withdraw(25).withdraw(15).withdraw(50).withdraw(15).yield_interest().display_account_info()




