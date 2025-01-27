#  Write a function to find the result

def my_res():
    res = int(input("Check you're marks: "))
    if res > 90:
        print("A++")
    elif res > 80:
        print("A+")
    elif res > 70:
        print("B") 
    elif res > 50:
        print("C") 
    elif res >= 33:
        print("D")
    else:
        print("Fail")  
my_res()                   
            