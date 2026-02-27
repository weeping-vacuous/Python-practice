from abc import ABC, abstractmethod

class Shape: 

    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius**2

class Square(Shape):
    def __init__(self,width):
         self.width = width
    
    def area(self):
        return self.width**2

class Triangle(Shape):
    def __init__(self,base,height):
        self.base= base
        self.height=height
    def area(self):
        return self.base*self.height*0.5
    
class Pizza(Circle):
    def __init__(self,topping,radius):
        self.topping= topping
        super().__init__(radius)

shapes=[Circle(4),Square(5),Triangle(6,7),Pizza("Pepperoni",3.5)]

for shape in shapes:
    print(f"{shape.area()} sq cm")