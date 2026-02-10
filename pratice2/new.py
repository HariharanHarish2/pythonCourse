from abc import ABC, abstractmethod

# Base User Class

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def login(self):
        print(f"{self.name} login successful ")


# Patient Class

class Patient(User):
    def __init__(self, name, email, health_id):
        super().__init__(name, email)
        self.__health_id = health_id

    def get_health_id(self):
        return self.__health_id

    def set_health_id(self, new_id):
        if len(new_id) >= 5:
            self.__health_id = new_id
            print("Health ID updated successfully ")
        else:
            print("Invalid Health ID ")

    def show_details(self):
        print("\n--- Patient Details ---")
        print("Name:", self.name)
        print("Email:", self.email)
        print("Health ID:", self.__health_id)


# Doctor Class (No Experience)

class Doctor(User):
    def __init__(self, name, email, specialization):
        super().__init__(name, email)
        self.specialization = specialization

    def show_details(self):
        print("\n--- Doctor Details ---")
        print("Name:", self.name)
        print("Email:", self.email)
        print("Specialization:", self.specialization)

    def __str__(self):
        return f"Dr {self.name} — {self.specialization}"

    def choose_consultation(self, choice):
        if choice == "general":
            return GeneralCheckup()
        elif choice == "surgery":
            return SpecialistSurgery()
        else:
            print("Invalid choice ")
            return None



# Consultation (Abstract)

class Consultation(ABC):
    @abstractmethod
    def prescribe(self):
        pass


class GeneralCheckup(Consultation):
    def prescribe(self):
        print("Prescription: Vitamins + Rest ")


class SpecialistSurgery(Consultation):
    def prescribe(self):
        print("Prescription: Surgery Procedure ")



# Patient Input
p_name = input("Enter patient name: ")
p_email = input("Enter patient email: ")
p_health = input("Enter health id: ")

patient = Patient(p_name, p_email, p_health)
patient.login()
patient.show_details()

# Update health id
new_id = input("\nEnter new health id to update: ")
patient.set_health_id(new_id)
print("Updated Health ID:", patient.get_health_id())


#  Doctor Input 
print("\nEnter Doctor Details")
d_name = input("Doctor name: ")
d_email = input("Doctor email: ")
d_spec = input("Specialization: ")

doctor = Doctor(d_name, d_email, d_spec)
doctor.login()
doctor.show_details()

print("\nDoctor Profile:", doctor)


#  Consultation 
choice = input("\nChoose consultation (general/surgery): ")
consult = doctor.choose_consultation(choice)

if consult:
    consult.prescribe()
