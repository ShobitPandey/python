class student:
    college_name = "Pt.DDUMC"
    @staticmethod
    def sec_A():
        return ("section A , CR name...")

    @staticmethod
    def sec_B():
        return ("section B , CR name...")    

class BCA(student):
    def __init__(self,name):
        self.name = name

s1 = BCA("Mr. Abhinav")
s2 = BCA("Mr. Shobit Pandey")

print(s1.sec_A())
print(s2.sec_B())
print(s1.name)
print(s2.name)
print(s1.college_name)