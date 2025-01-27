"""
Create student class that takes name & marks of 3 subjects as arguments in constructor.
Then create a method to print the average
"""

class student:
    def __init__(self,name, marks):
        self.name = name
        self.marks = marks
     
    @staticmethod
    def hello():
        print("hello")

    @staticmethod
    def age():
        print("age")

    def average(self):
        sum = 0
        for value in self.marks:
            sum = sum + value
        print("Hey",self.name,"you're average score is: " , sum/3)

            
s1 = student("Shobit Pandey", [68, 85, 100])
s1.average()
s1.hello()
s1.age()


# s1.name = "Niharika Pandey"
# s1.average()


# class student:

#     college_name = "Pt.DDUMC"
#     print(college_name)

#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def welcome(self):
#         print("welcome student,",self.name)

#     def marks(self):
#         return self.marks
        

# s1 = student("karan",97)
# s1.welcome()
# print(s1.marks)

# # s1 = student()
# # print(s1.name)

# # s2 = student()
# # print(s2.name)

# # class car:
# #     color = "red"
# #     brand = "tesla"
# # car1 = car()
# # print(car1.color) 
# # print(car1.brand)  
   
class animal:
    def bark(self):
        print("Dogs bark")

class dog(animal):
    def speak(self):
        print("animal speak")

dog = dog()
dog.speak()
dog.bark()