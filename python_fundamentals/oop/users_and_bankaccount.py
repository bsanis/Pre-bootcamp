class bankaccount:
    accounts = []

    def __init__(self,int_rate,balance=0,interest=0.00):
        self.int_rate = int_rate
        self.balance = balance
        self.interest = interest
        bankaccount.accounts.append(self)


class user:
    def __init__(self,first_name,last_name,email,age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.account = bankaccount(int_rate=0.02, balance=0)
    
    def make_deposit(self,amount):
        bankaccount.balance =  bankaccount.balance + amount
        return self
    
    def make_withdraw(self,amount):
        if amount < bankaccount.balance:
            bankaccount.balance = bankaccount.balance - amount
        else:
            print("account must be feeded !!")
        return self
    
    def display_user_balance(self):
        print(f"your balance : {bankaccount.balance}")
        return self
    
    print(display_user_balance)