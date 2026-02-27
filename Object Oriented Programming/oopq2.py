##2
class Student:
    def __init__(self):
        self._grade= None
    
    def set_grade(self,new_grade):
        if 0<=new_grade<=100:
            self._grade = new_grade
        else:
            print("The students grade must be between 0 and 100")

    def get_grade(self):
        return self._grade
    
student1=Student()
while True:
    grade=int(input("Enter student grade:"))
    student1.set_grade(grade)
    if student1.get_grade() is not None:
        print(student1.get_grade())
        break
    else:
        continue

        


    
