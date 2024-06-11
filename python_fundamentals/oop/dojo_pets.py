class ninja:
    def __init__(self,first_name,last_name,pet,treats,pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pet
        self.treats = treats
        self.pet_food = pet_food

# implement __init__( first_name , last_name , treats , pet_food , pet )
# implement the following methods:
# walk() - walks the ninja's pet invoking the pet play() method
# feed() - feeds the ninja's pet invoking the pet eat() method
#bathe() - cleans the ninja's pet invoking the pet noise() method

    def walk(self):
        self.pet.play()
        print(f"ninja playing with{pet.name}")

    def feed(self):
        self.feed = pet.eat()
        print(f"{pet.name} eats")
    
    def bathe(self):
        self.pet.noise()
        print(f"{pet.noise}")


# implement __init__( name , type , tricks ):
# implement the following methods:
# sleep() - increases the pets energy by 25
# eat() - increases the pet's energy by 5 & health by 10
# play() - increases the pet's health by 5
# noise() - prints out the pet's sound


class pet:
    def __init__(self,name,type,tricks,health = 100,energy = 50):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy

    def sleep(self):
        energy += 25
        return self

    def eat(self):
        energy += 5
        health += 10
        return self
    
    def play(self):
        health += 5
        return self

    def noise(self):
        print(self.noise)


malek = ninja("malek","ben selma",pet.name,pet.play,ninja.pet_food)
malek.feed()
malek.walk()
malek.bathe()







