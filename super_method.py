"""
Super method
super() method is used to access methods of the parent class.
"""

class car:
    def __init__(self,type):
        self.type = type 

    @staticmethod
    def start():
        print("car started...")

    @staticmethod
    def stop():
        print("car stopped")

class Toyota_car(car):
    def __init__(self, type):
        super().__init__(type)
        self.type
        super().start()

car1 = Toyota_car("prius ,Electric")
print(car1.start())


        