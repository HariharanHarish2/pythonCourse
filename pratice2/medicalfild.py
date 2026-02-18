    
# Step 1: Import Abstraction tool

from abc import ABC, abstractmethod



# Step 2: Base Class (Inheritance)

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def login(self):
        print(f"{self.name} logged in successfully")



# Step 3: Patient Class (Encapsulation)

class Patient(User):
    def __init__(self, name, email, health_id):
        super().__init__(name, email)
        self.__health_id = health_id  # private variable

    # Getter
    def get_health_id(self):
        return self.__health_id

    # Setter with validation
    def set_health_id(self, new_id):
        if len(new_id) >= 5:
            self.__health_id = new_id
            print("Health ID updated successfully")
        else:
            print("Invalid Health ID")



# Step 4: Doctor Class (__str__)

class Doctor(User):
    def __init__(self, name, email, specialization):
        super().__init__(name, email)
        self.specialization = specialization

    def __str__(self):
        return f"Dr. {self.name} - {self.specialization}"



# Step 5: Abstract Class (Abstraction)

class Consultation(ABC):

    @abstractmethod
    def prescribe(self):
        pass


# Step 6: Polymorphism Classes

class GeneralCheckup(Consultation):
    def prescribe(self):
        print("Prescribed vitamins and regular exercise")


class SpecialistSurgery(Consultation):
    def prescribe(self):
        print("Prescribed surgery procedure and post-care")


# Step 7: Simulation (Polymorphism_)
doctor = Doctor("Ramesh", "ramesh@hospital.com", "Cardiologist")
patient = Patient("Suresh", "suresh@gmail.com", "H12345")

print(doctor)
patient.login()

print("Patient Health ID:", patient.get_health_id())

consultations = [
    GeneralCheckup(),
    SpecialistSurgery()
]

for consult in consultations:
    consult.prescribe()
