#task 0
from abc import ABC ,abstractmethod

# task 1
class user:
    def __init__(self,name,email):
        self.name = input("name:")
        self.email = input("email:")

    def login(self):
        print(f"{self.name} confirmation message")


#Task 2
class patient(user):
    def __init__(self,name,email,health_id):
        super().__init__(name,email)
        self.__health_id = health_id

    def get_health_id(self):
        return self.__health_id
    
    def set_health_id(self,new_id):
       if len(new_id)>=5:
         self.__health_id=new_id
         print("Health id is update sucessfully")
       else:
           print("Invalid Heath_id")


#Task 3
class doctor(user):
    def __init__(self,name,email,Specialization):
        super().__init__(name,email)
        self.Specialization = Specialization

    def __str__(self):
        return f"Dr {self.name} - {self.Specialization}"

    # doctor  consultation
    def choose_consultation(self, choice):
        if choice == "general":
            return GeneralCheckup()
        elif choice == "surgery":
            return SpecialistSurgery()
        else:
            print("Invalid choice")
            return None


#Task 4
class Consultation(ABC):

    @abstractmethod
    def Prescribe(self):
        pass


class GeneralCheckup(Consultation):
    def Prescribe(self):
        print("General suggests vitamins")


class SpecialistSurgery(Consultation):
    def Prescribe(self):
        print("Specialist suggests a procedure")


#Task 6
Doctor = doctor("Hari","Hari@gmail.com","Bone specialist")
Patient = patient("Arun","Arun@123","No127E")


Patient.login()
print("Patient Health_id:", Patient.get_health_id())

Patient.set_health_id("N444H3")
print("Update Health_id:", Patient.get_health_id())

print(Doctor)
#Task 7
choice = input("Doctor choose consultation (general/surgery): ")

consult = Doctor.choose_consultation(choice)

if consult:
    consult.Prescribe()
