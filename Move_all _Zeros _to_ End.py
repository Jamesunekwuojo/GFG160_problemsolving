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
