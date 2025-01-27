# Add two numbers provided by the user 
class number:

    @staticmethod
    def sum_numbers():
        
        first_number = int(input("Enter first number: "))
        second_number = int(input("Enter second number: "))
        sum = first_number + second_number
        print(sum)

number.sum_numbers()