"""
Define an emp class  with attributes role, department & salary This class also has a showdetails() method.
Create an Engineer class that inherits properties from Employee & F
attributes : name & age.
"""
class employee:
    def __init__(self, role , deprt, sal):
        self.role = role
        self.deprt = deprt
        self.sal = sal

    def ShowDetails(self):
            print ("role =", self. role)
            print ("dept =", self.deprt)
            print("salary =", self .sal)

emp1 = employee("Accountant", "Finance", "rs")