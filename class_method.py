"""
class method
A class method is bound to the class & receives the class as an implicit first argument.
Note - static method can't access or modify class state & generally for utility.
class Student: 
    @classmethod # decorator
    def college( cls):
         pass
"""

class person:
    name = "ananoyums"
    @classmethod
    def changeName(cls,name):
        cls.name = name

p1 = person()
p1.changeName("Shobit Pandey")
print(p1.name)
print(person.name)
