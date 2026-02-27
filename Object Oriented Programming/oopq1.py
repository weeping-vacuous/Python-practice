##1 classes and objects
class Car:
    def __init__(self,model,year):
        self.model= model
        self.year=year

    def get_desciption(self):
        print(f"{self.year} {self.model}")

car1=Car("Toyota",2024)
car2=Car("Ferrai",2021)

if __name__ =="__main__":
    car1.get_desciption()
    car2.get_desciption()