class Student:
    def __init__(self, name):
        self.name = name

    def study(self):   # method
        print(self.name, "is studying")
s1 = Student("Hari")
s1.study()
