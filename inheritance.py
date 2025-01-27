"""

Inheritance
When one class(child/derived derives the properties & methods of another class(parent/base)

"""

class car:
    color = "red"
    @staticmethod
    def start():
        print("Car started...")

    @staticmethod
    def stop():
        print("stop car...")    

class Toyota_car(car):
    def __init__(self,name):
        self.name = name

car1 = Toyota_car("Fortuiner")
car2 = Toyota_car("prius")

print(car1.stop())
print(car2.name)
print(car1.color)
        