
"""
Given an array arr[]. Rotate the array to the left (counter-clockwise direction) by d steps, where d is a positive integer. 
Do the mentioned change in the array in place.
Note: Consider the array as circular.
"""
# E.g if we have an array like  arr[] = [1, 2, 3, 4, 5]...
# If the array is rotating in the left direction by 1, will look like this:
# [2, 3, 4, 5, 1]..


# '1' will go back and then any other element will shoft their position by one.

**APPROACHES**
Approach 1: Performing 1 left shift d times
complexity for this appraoch are:Time complexity is O(n) it will take O(n *d) whuch is not the best.
