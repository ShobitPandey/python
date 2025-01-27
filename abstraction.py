
# Abstraction ----> Hiding the implementation details of a class and only showing the essential features to the user.
# Encapsulation -----> Wrapping data and functions into a single unit (object).
# class car:
#     def __init__(self):
#         self.acc = False
#         self.brk = False
#         self.clutch = False
  
        
#     def start(self):
#         self.clutch = True
#         self.acc = True
#         print("Car Starterd...")

# car1 = car()
# car1.start()


# --------------------------------------------------------------------------------------------------------------
"""""
Create Account class with 2 attributes - balance & account no. Create methods for debit, credit & printing
the balance.
"""

class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc

    # Debit Method
    def debit(self, amount):
        self.balance = self.balance - amount
        print("Rs.", amount, "was debited")
        print("Total amount = ", self.get_balance())

    # Credit Method
    def credit(self, amount):
        self.balance = self.balance + amount
        print("Rs.", amount, "was credited")
        print("Total amount = ", self.get_balance())

    def get_balance(self):
        return self.balance


acc1 = Account(25000 , 12345)
acc1.debit(2000)
acc1.credit(10000)
acc1.credit(100000)
# print("You're Current Account Balance is: " + str(acc1.balance))
# print("You're Account Number is: " + str(acc1.account_no))
    