class car:
    color = "red"
    @staticmethod
    def start():
        print("Car started...")

    @staticmethod
    def stop():
        print("stop car...")    

class Toyota_car(car):
    def __init__(self,brand):
        self.brand = brand

class Fortionuer(Toyota_car):
    def __init__(self, type):
        self.type = type
        

car1 = Fortionuer("Electric")
print(car1.start())
