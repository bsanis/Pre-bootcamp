class user:
    def __init__(self):
        self.first_name = "anis"
        self.last_name = "ben selma"
        self.age = 40
        
    print("Hi")
user_anis = user()
print(user_anis.first_name + " " +user_anis.last_name)
user_ahmed_youssef = user()
print("Hi mister" +" "+ user_ahmed_youssef.last_name)
print(user_anis.age)

class shoe:
    def __init__(self,brand,shoe_type,price):
        self.brand = brand
        self.type = shoe_type
        self.price = price
        self.in_stock = True
    
    def discount(self,percent):
        self.price = self.price * (1 - percent)

skater_shoe = shoe("Nike","low-top trainers",90)
dress_shoe = shoe("Jack & Jill Bootery", "Ballet Flats", 50)
print(skater_shoe.type)
print(dress_shoe.type)
print(skater_shoe.price)
skater_shoe.discount(0.3)
print(dress_shoe.price)
dress_shoe.discount(0.5)
print(dress_shoe.price)

'''
class Shoe:

    def __init__(self, brand, shoe_type, price):
        self.brand = brand
        self.type = shoe_type
        self.price = price
        self.in_stock = True
    
    # Takes a float/percent as an argument and reduces the
    # price of the item by that percentage.
    def on_sale_by_percent(self, percent_off):
        self.price = self.price * (1-percent_off)
    
    # Returns a total with tax added to the price.
    def total_with_tax(self, tax_rate):
        tax = self.price * tax_rate
        total = self.price + tax
        return total
    
    # Reduces the price by a fixed dollar amount.
    def cut_price_by(self, amount):
    	if amount < self.price:
        	self.price -= amount
    	else:
    		print("Price deduction too large.")

# Create some shoes. Call some methods on those shoes. Print your shoe's attributes..
my_shoe = Shoe("Converse", "Low-tops", 36.00)
print(my_shoe.total_with_tax(0.05))
my_shoe.cut_price_by(10)
print(my_shoe.price)
'''






class user:
    def __init__(self,name,phone):
        self.name = name
        self.phone = phone
    
    def greetings(self):
        print(f"hello,my name is {self.name}")
anis = user("Anis",50816064)
anis.greetings()