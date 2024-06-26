class bank_account:
    # class attributes
    bank_name = "First national Dojo"
    #new class attribute : list of all accounts
    all_accounts = []

    def __init__(self,int_rate,balance) :
        self.int_rate = int_rate
        self.balance = balance
        bank_account.all_accounts.append(self)
    
    #class method to change name of the bank
    @classmethod
    def change_bank_name(cls,name):
        cls.change_bank_name = name

    # class method to get balance of all accounts
    @classmethod
    def all_balance(cls):
        sum = 0
        # we use cls to refer to the class
        for account in cls.all_accounts:
            sum += account.balance
            return sum
        

class BankAccount:
    def __init__(self,int_rate,balance) :
        self.int_rate = int_rate
        self.balance = balance
        bank_account.all_accounts.append(self)
    def with_draw(self,amount):
        # we can use the static method here to evaluate
        # if we can with draw the funds without going negative
        if BankAccount.can_withdraw(self.balance,amount):
            self.balance -= amount
        else:
            print("Insufficient Funds")
        return self
    # static methods have no access to any attribute
    # only to what is passed into it
    @staticmethod
    def can_withdraw(balance,amount):
    	if (balance - amount) < 0:
            return False
        else:
            return True
