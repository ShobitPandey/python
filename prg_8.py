#  Write a function in array which return the largest number in array.

def find_larfgest_num(arr):
    if len(arr) == 0:
        return  "Invalid"
    largest_number = arr[0]
    for num in arr:
        if num in arr:
            largest_number = num
    return largest_number
arr = [ 10,55,56,14,100,178]
my_largest_num = find_larfgest_num(arr)
print(my_largest_num)        