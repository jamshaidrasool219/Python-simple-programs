# Program: Class aur Object
class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def show(self):
        print(f"Naam: {self.name}, Roll No: {self.roll_no}")


s1 = Student("Ali", 1)
s2 = Student("Ahmed", 2)

s1.show()
s2.show()
