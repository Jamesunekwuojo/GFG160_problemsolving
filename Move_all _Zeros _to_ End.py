"""
DAY 2
You are given an array arr[] of non-negative integers. Your task is to move all the zeros in the array to the right end while maintaining 
the relative order of the non-zero elements. 
The operation must be performed in place, meaning you should not use extra space for another array.
"""

# **APPROCH USED TO SOLVE PROBLEMS** 
# They are mansy approcahes that can be used to solve the problem, but the most optimized one with the minimialist
# amd less time complexity and space complesity is going to be used.
  
# Approch Idea: A varibale(pointer) would be created to keep in check/track where the next non zeroth element  in the array is going to be kept.
# When a non zeroth elemt is encountered, instead of placing that element at directly at  arr[count] it would be swapped with the array arr[count]
# This ensures that if they is any zeroth element at arr[count] it would be pushed to the end, not overwritten.

# Time complexities: O(n) --> only one Iteration needed.
# Space complexites: O(1) --> no extra space created, 
# Algorithm:
# Step 1: Create a Pointer to track the position for next non-zero element
# Step 2: Create a loop (for) to interate thru the array
# Step 3: Check if the current elemt at i !=0, THEN swap current element with the 0 at index 'count'
# Step  4: Move 'count' pointer to the next position.
def pushZerosEnd(arr):
  count = 0
  for i in range(len(arr)):
      if arr[i] != 0:
        
        arr[1], arr[count] = arr[count], arr[1]
        count +=1

if __name__ == "__main__":
    arr = [1, 2, 0, 4, 3, 0, 5, 0]
    pushZerosToEnd(arr)
        
          




    
