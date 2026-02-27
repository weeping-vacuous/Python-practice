#duck typing

class Animal:
    alive = True

class Dog(Animal):
    def speak(self):
        print("WOOF!")

class Cat(Animal):
    def speak(self):
        print("MEOW!")

class Car:
    alive = True
    def speak(slef):
        print("HONK!")

animals=[Dog(),Cat(),Car()]

for animal in animals:
    animal.speak()
    print(animal.alive)