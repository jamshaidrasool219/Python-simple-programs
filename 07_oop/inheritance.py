# Program: Inheritance
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} awaaz nikalta hai")


class Dog(Animal):
    def speak(self):
        print(f"{self.name}: Bhow bhow!")


class Cat(Animal):
    def speak(self):
        print(f"{self.name}: Meow!")


for pet in [Dog("Tommy"), Cat("Kitty"), Animal("Janwar")]:
    pet.speak()
