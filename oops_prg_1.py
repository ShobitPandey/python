"""
Qs. Define a Circle class to create a circle with radius r using the constructor.
Define an Area method of the class which calculates the area of the circle. Define a Perimeter method of the class which allows you to calculate the perimeter of the
circle.
"""

class circle:
    def __init__(self, rad):
        self.rad = rad

    def area(self):
        return 3.14 * 21 * 21
    
    def per(self):
        return 2 * 3.14 * self.rad

c1 = circle(21)
print(c1.area())
print(c1.per())