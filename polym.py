"""
Polymorphism: Operator Overloading
When the same operator is allowed to have different meaning according to the context.

Operators & Dunder functions
     a + b #addition
     a - b #subtraction
     a * b #multiplication
     a l b #division
     a % b #addition
     a._add _ (b)
     a. _ sub_ (b)
     a. _ mul___ (b)
     a. _ truediv _ _ _ (b)
     a._ _ mod _ - _ (b)
"""


# print (1 + 2) #3
# print(type(1))
# print ("apna" + "college") #concatenate
# print(type("appna"))
# print([1, 2, 3] + [4, 5, 6]) #merge
# print(type([1,2,3]))

class complex:
    def __init__(self , real , img):
        self.real = real
        self.img = img

    def showNumber(self):
        print (self. real, "i +", self. img, "j")

    def __add__(num1 , num2):
        newReal = num1.real  + num2.real
        newImg = num1.img  + num2.img
        return complex(newReal, newImg )
    
    def __sub__(num1 , num2):
        newReal = num1.real  - num2.real
        newImg = num1.img  - num2.img
        return complex(newReal, newImg )

num1 = complex(1 , 2)
num1.showNumber()

num2 = complex(10 , 15)
num2.showNumber()

num3 = num1 + num2
# num3 = num1.add(num2)
num3.showNumber()

num3 = num1 - num2
num3.showNumber()