class Student:
    def __init__(self, name, roll) :
        self.name = name
        self.roll = roll
    
    def stud_det(self):
        print("name : ", self.name)
        print("age : ", self.age)

class Student1(Student):
    def __init__(self, age):
        self.age = age

obj = Student1(20)
obj.stud_det()
