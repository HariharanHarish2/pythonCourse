from abc import ABC ,abstractmethod
class car(ABC):
    @abstractmethod
    def moveforward(self):
        pass
    
    @abstractmethod
    def backforward(self):
        pass

    @abstractmethod
    def rightside(self):
        pass

    @abstractmethod
    def leftside(self):
        pass
class swift(car):
    def moveforward(self):
        print("moveforward this car")
    def backforward(self):
        print("backforward this car")
    def rightside(self):
         print("rightside this car")
    def leftside(self):
         print("leftside this car")

class thar(car):
    def moveforward(self):
        print("  thar moveforward this car")
    def backforward(self):
        print(" thar backforward this car")
    def rightside(self):
         print(" thar rightside this car")
    def leftside(self):
         print("thar leftside this car")

company =thar()
company.moveforward()
