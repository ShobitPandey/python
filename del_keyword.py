"""""
del kevword

Used to delete object properties or object itself. 

del si.name
del s1

"""
class student:
    def __init__(self,name):
        self.name = name

s1 = student("Shobit")
print(s1.name)

del s1.name
del s1  
print(s1.name)