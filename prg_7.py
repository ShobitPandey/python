# WAP to count even  array.
count = 0
def count_even_arr(arr):
    for num in arr:
        global count
        if num % 2 == 0:
            count = count + 1
    print(count)
arr = [1,2,3,4,5,6,7,8,9,10,12]
count_even_arr(arr)            