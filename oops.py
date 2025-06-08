
class employee:

    def __init__(self):
        print("Started Executing Attributes")
        self.id=123
        self.salary=50000
        self.name="John"
        print("Attributes has been initiat,ed") 

    def display(self,des):
        print("This Function was called manulllay")
        print(f"Employee ID: {self.id}")
        print(f"Salary Of the Employee : {self.salary}")
        print(f"Name Of the Employee : {self.name}")
        print(f"{self.name} is Travelling to {des}")

obj=employee()
obj.name ="sam kumar"
#display('chennai')