# Find the 1 based position of the first occurence of k in the array arr , or return -1 if k is not present.

from typing import List
class solution:
    def search(self, k: int, arr: list[int])->int:
        for i in range(len(arr)):
            if arr[i] == k:
                return i + 1
            return 1 
   