class Student:

    count = 0
    Total_GPA = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.Total_GPA += gpa

    #INSTANCE METHOD
    def get_info(self):
        return f"{self.name} has a GPA of {self.gpa}"
    
    #CLASS METHODS
    @classmethod
    def get_count(cls):
        return f"There are {cls.count} students"
    
    @classmethod
    def get_average_gpa(cls):
        if cls.count == 0:
            return 0
        return f"{ cls.Total_GPA / cls.count:.2f} is the average GPA"
    

student1 = Student("Spongebob", 3.5)
student2 = Student("Patrick", 3.8)
student3 = Student("Squidward", 2.5)
student4 = Student("Sandy", 3.9)    
print(Student.get_count())
print(Student.get_average_gpa())