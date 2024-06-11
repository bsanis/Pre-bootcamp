import urllib.request
response = urllib.request.urlopen("http://www.codingdojo.com")
html = response.read()
print(html)


class Parent:
    def method_a(self):
        print("invoking PARENT method_a!")
class Child(Parent):
    def method_a(self):
        print("invoking CHILD method_a!")
dad = Parent()
son = Child()
dad.method_a()
son.method_a() #notice this overrides the Parent method!




'''
class BankAccount:
    def withdraw(self, amount):
    if (self.balance - amount) > 0:
	self.balance -= amount
    else:
    print("INSUFFICIENT FUNDS")
	return self

class RetirementAccount(BankAccount):
    def withdraw(self, amount, is_early):
    if is_early:
        amount = amount * 1.10
    super().withdraw(amount)
    return self
    '''






