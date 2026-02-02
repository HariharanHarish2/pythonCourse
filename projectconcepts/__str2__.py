class Student:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Student name is {self.name}"
s=Student("Hari")
print(s)
