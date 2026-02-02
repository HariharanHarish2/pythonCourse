class Animal:
    def sound(self):
        print("Animal makes sound")

class Dog(Animal):   # Inheritance
    def bar(self):
        print("Dog barks")
s=Dog()
s.sound()
s.bar()