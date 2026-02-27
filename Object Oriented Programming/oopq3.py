##3

class Animal:
    def __init__(self,name,species):
        self.name = name
        self.species = species

    def make_sound(self):
        print("GRRR")

class Dog(Animal):
    def __init__(self,name):
        super().__init__(name, "Dog")

    def make_sound(self):
        print("WOOF!!")

class Cat(Animal):
    def __init__(self,name):
        super().__init__(name, "Cat")

    def make_sound(self):
        print("MEOW!!")

dog=Dog("Milo","Dog")
cat=Cat("Bond","Cat")

print(f"{dog.name} is {dog.species} and he goes:",end=" ")
dog.make_sound()
print(f"{cat.name} is {cat.species} and he goes:",end=" ")
cat.make_sound()
