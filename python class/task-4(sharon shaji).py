import math
questions = """
1. Write a Python class which has two methods get_String and print_String. get_String accept a string from the user and print_String print the string in upper case.

2. Write a Python class named Circle constructed by a radius and two methods which will compute the area and the perimeter of a circle.

3. Create a Student class and initialize it with name and roll number. Make methods to :
a. Display - It should display all informations of the student.
b. setAge - It should assign age to student
c. setMarks - It should assign marks to the student.

4. Create a Time class and initialize it with hours and minutes.
a. Make a method addTime which should take two time object and add them. E.g.- (2 hour and 50 min)+(1 hr and 20 min) is (4 hr and 10 min)
b. Make a method displayTime which should print the time.
c. Make a method DisplayMinute which should display the total minutes in the Time. E.g.- (1 hr 2 min) should display 62 minute

"""

questions_list = [item.strip() for item in questions.split("\n\n") if item.strip()]

def getQuestion(index):
    index-=1
    print("\n",questions_list[index], "\n")
    

class MyString :

    def __init__(self, userString):
        self.string = userString
    
    def get_string(self, string):
        print("you entered -> ", string)
    
    def print_string(self):
        print("your string in uppercase - ", self.string.upper())

class Circle: 
    def __init__(self, radius):
        self.radius = radius
    
    def get_area(self):
        return math.pi * (self.radius ** 2)
    
    def get_perimeter(self):
        return 2 * math.pi * self.radius

class Student: 
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno

    def display_student(self):
        return f"Name : {self.name}, roll number : {self.rollno}"

    def set_age(self, age):
        self.age = age

    def set_mark(self, mark):
        self.mark = mark

class Time:
    def __init__(self, hour, minutes):
        self.hour = hour
        self.minutes = minutes

    def get_time(self):
        print(f"\nentered time : {self.hour} hour & {self.minutes} minutes")


    def add_time(self, other_time):
        total_hour = (self.hour + other_time.hour) + ((self.minutes + other_time.minutes) // 60)
        total_min = (self.minutes + other_time.minutes) % 60
        print(f"\nadded time : {total_hour} hour & {total_min} minutes")
    
    def display_time_in_minutes(self, other_time):
        total_minutes = ((self.hour + other_time.hour) * 60) + (self.minutes + other_time.minutes)
        print(f"\nTotal minutes = {total_minutes}")

def main():
    while True:
        try:
            choice = int(input("Enter a question number or enter \033[31m 0 \033[0m to Quit : "))
            if choice == 0:
                print("Quitting...")
                break;
            elif 0 < choice <= 4 :
                getQuestion(choice)
                if choice == 1:
                    string = input("Enter a string : ")
                    st = MyString(string)
                    st.get_string(string)
                    st.print_string()
                    print("\n")
                elif choice == 2:
                    radius = float(input("Enter a radius : "))
                    st = Circle(radius)
                    print(f"Area = {st.get_area()} & perimeter = {st.get_perimeter()}")
                    print("\n")
                elif choice == 3:
                    name = input("Enter name : ")
                    rollno = int(input("Enter roll number : "))
                    st = Student(name, rollno)
                    print(f"student info (initial) = {st.display_student()}")
                    age = int(input("Enter age : "))
                    mark = float(input("Enter mark : "))
                    st.set_age(age)
                    st.set_mark(mark)
                    print(f"student info (final) = {st.display_student()}, age : {st.age}, mark : {st.mark}")
                    print("\n")
                elif choice == 4:
                    hour = int(input("Enter hour : "))
                    minute = int(input("Enter minute : "))
                    time = Time(hour=hour, minutes=minute)
                    time.get_time()
                    other_hour = int(input("Enter new hour1 : "))
                    other_minute = int(input("Enter new minute1 : "))
                    other_time = Time(other_hour,other_minute)
                    time.add_time(other_time)
                    time.display_time_in_minutes(other_time)
                    print("\n")
            else :
                print("Invalid Input. Please Retry...")

        except ValueError:
            print("Invalid Input. Please Retry...")
            
if __name__ == "__main__":
    main()
