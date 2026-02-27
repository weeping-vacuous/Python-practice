class Animal:
    def __init__(self,name):
        self.name=name
        self.is_alive = True
    
    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal):
    def speak(slef):
        print("WOOF!")

class Cat(Animal):
    def speak(slef):
        print("MEOW!")

class Mouse(Animal):
    def speak(slef):
        print("SQUEAK!")

dog=Dog("Scooby")
cat=Cat("Garfield")
mouse=Mouse("Jerry")

class Prey(Animal):
    def flee(self):
        print(f"{self.name}  is fleeing")

class Predator(Animal):
    def hunt(self):
        print(f"{self.name}  is hunting")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey,Predator):
    pass

fish=Fish("Nemo")
print(fish.is_alive)