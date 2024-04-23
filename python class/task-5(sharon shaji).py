import datetime

questions = """

1. Demonstrate Simple inheritance for Arithmetic class
2. Demonstrate Multilevel inheritance for Employee class
3. Demonstrate Multiple inheritance for Student class
4. Demonstrate Heirarchial inheritance for Polygon class

"""

questions_list = questions.strip().split("\n")

def getQuestion(index):
    index-=1
    print("\n",questions_list[index], "\n")
    

class ColorString(object):
    def __init__(self, string):
        self.string = str(string)
        self.reset = '\033[0m'
        self.color = {
            'red': '\033[31m',
            'black': '\033[30m',
            'green': '\033[32m',
            'yellow': '\033[33m',
            'blue': '\033[34m',
            'magenta': '\033[35m',
            'cyan': '\033[36m',
            'white': '\033[37m',
        }

    def __getattr__(self, attr):
        # Check if the attribute being accessed is the one you want to dynamically implement
        if attr.lower() in self.color:
            return f"{self.color[attr.lower()]}{self.string}{self.reset}"
        else:
            # For other attributes, raise AttributeError as usual
            raise AttributeError(f"'{self.__name__}' object has no attribute '{attr}'")

# * Question 1 start --------------------------------------------------------
class Arithmetics():
    def __init__(self,num1, num2):
        self.num1 = num1
        self.num2 = num2


class Arithmetic_operations(Arithmetics):
    def __init__(self, num1, num2):
        super().__init__(num1, num2)
        print(f"The numbers are : {ColorString(self.num1).green} & {ColorString(self.num2).green}")

    add = lambda self: print(f"Addition = {ColorString(self.num1 + self.num2).blue}")
    subtract = lambda self : print(f"Subtraction {ColorString(self.num1 - self.num2).blue}")
    multiply = lambda self : print(f"Multiplication = {ColorString(self.num1 * self.num2).blue}")
    def divide(self):
        if self.num1 != 0:
            print(f"Division = {ColorString(self.num1 / self.num2).blue}")
        else: 
            print(ColorString("Cannot divide by 0").red)

# * Question 1 end --------------------------------------------------------

# ? Question 2 start --------------------------------------------------------

class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def BasicInfo(self):
        print(f"Name : {ColorString(self.name).yellow} {ColorString("&").blue} Age : {ColorString(self.age).yellow}")

class EmployeePost(Employee):
    def __init__(self, name, age, post, salary):
        super().__init__(name, age)
        self.post = post
        self.salary = salary

    def postInfo(self): 
        print(f"{ColorString(self.name).yellow} has been given a post of {ColorString(self.post).yellow} with {ColorString(self.salary).yellow} as salary")

class EmployeeServiceBook(EmployeePost):
    def __init__(self, name, age, post, salary, experience, join_year, is_retired):
        super().__init__(name, age, post, salary)
        self.experience = experience
        self.join_year = join_year
        self.is_retired = is_retired

    def full_details(self):
        print(f"""\nName = {ColorString(self.name).magenta}
Age = {ColorString(self.age).magenta}
post = {ColorString(self.post).magenta}
salary = {ColorString(self.salary).magenta}
experience = {ColorString(self.experience).magenta}
join_year = {ColorString(self.join_year).magenta}
is_retired = {ColorString(self.is_retired).magenta}
""")

    def service_history(self):
        working_status = "had worked" if self.is_retired else "has been working"
        print(f"{ColorString(self.name).yellow} {working_status} as a {ColorString(self.experience).yellow} {ColorString(self.post).yellow} for {ColorString(datetime.date.today().year - int(self.join_year)).yellow} years with a salary of {ColorString(self.salary).yellow}. {ColorString(self.name).yellow} is {ColorString(self.age).yellow} years old.")

# ? Question 2 end --------------------------------------------------------

# * Question 3 start --------------------------------------------------------
class Student:
    def __init__(self, name, rollnumber):
        self.name = name
        self.rollnumber = rollnumber

    @staticmethod
    def display_student_info(name, rollnumber):
        print(f"Name: {ColorString(name).blue}, Rollnumber: {ColorString(rollnumber).blue}")

class Course:
    def __init__(self, course_name, is_completed) -> None:
        self.course_name = course_name
        self.is_completed = is_completed

    @staticmethod
    def display_course_info(course_name, is_completed):
        status = "Completed" if is_completed else "Ongoing"
        print(f"Course: {ColorString(course_name).blue}, Course Status: {ColorString(status).cyan if is_completed else ColorString(status).magenta}")

class StudentCertificate(Student, Course):
    def __init__(self, name, rollnumber, course_name, is_completed):
        Student.__init__(self,name, rollnumber)
        Course.__init__(self,course_name, is_completed)


    def display_certificate_info(self):
        Student.display_student_info(self.name, self.rollnumber)
        Course.display_course_info(self.course_name, self.is_completed)
        if self.is_completed: 
            print("\nCertificate Successfully Issued!")
        else :
            print("\nCertificate Issue Failed!")
            print(f"{ColorString(self.name).yellow} is not {ColorString("passed!").red}")
    
# * Question 3 end --------------------------------------------------------

# ? Question 4 start --------------------------------------------------------
class Polygon:
    def __init__(self, polygon_type):
        self.polygon_type = polygon_type

    def get_area(self):
        pass

class Triangle(Polygon):
    def __init__(self, base, height):
        super().__init__("Triangle")
        self.base = base
        self.height = height

    def get_area(self):
        print(f"Area of {self.polygon_type} is {ColorString(0.5 * self.base * self.height).yellow}")
        

class Rectangle(Polygon):
    def __init__(self, length, width):
        super().__init__("Rectangle")
        self.length = length
        self.width = width

    def get_area(self):
        print(f"Area of {self.polygon_type} is {ColorString(self.length * self.width).yellow}")

# ? Question 4 end --------------------------------------------------------

def main():
    print(ColorString("[ The program uses hard-coded values for task purpose ]").green)
    while True:
        try:
            choice = int(input(f"Enter a question number {ColorString('[1 to 4]').cyan} or enter {ColorString('0').red} to Quit : "))
            if choice == 0:
                print("Quitting...")
                break;
            elif 0 < choice <= 4 :
                getQuestion(choice)
                if choice == 1:
                    operation = Arithmetic_operations(0,20)
                    operation.add()
                    operation.subtract()
                    operation.multiply()
                    operation.divide()
                elif choice == 2:
                    employee = EmployeeServiceBook(name="Arthur", age="30", post="Cowboy", experience="Veteran", join_year="2017", salary="5000000", is_retired=True)
                    #employee.BasicInfo()
                    #employee.postInfo()
                    employee.full_details()
                    employee.service_history()
                elif choice == 3:
                    certificate = StudentCertificate("Tony", 1, "Robotics", True)
                    certificate.display_certificate_info()
                    print("\n")
                elif choice == 4:
                    print(f"The values are : {ColorString('10').cyan} and {ColorString('20').cyan}")
                    triangle = Triangle(10, 20)
                    rectangle = Rectangle(10, 20)

                    triangle.get_area()
                    rectangle.get_area()
                    print("\n")
            else :
                print("Invalid Input. Please Retry...")

        except ValueError:
            print("Invalid Input. Please Retry...")
            
if __name__ == "__main__":
    main()