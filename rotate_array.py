
"""
Given an array arr[]. Rotate the array to the left (counter-clockwise direction) by d steps, where d is a positive integer. 
Do the mentioned change in the array in place.
Note: Consider the array as circular.
"""
# E.g if we have an array like  arr[] = [1, 2, 3, 4, 5]...
# If the array is rotating in the left direction by 1, will look like this:
# [2, 3, 4, 5, 1]..


# '1' will go back and then any other element will shoft their position by one.

# **APPROACHES**
# Approach 1: Performing 1 left shift d times
# complexity for this appraoch are:Time complexity is O(n) it will take O(n *d) whuch is not the best.
# Apprach 2:  Juggling Algorithmn
# gcd(greatest common divisor)
# gcd(length of array, d) ----> It meeans the gcd the highest common divisor of the 
# array and no of times (d) to rotate the array.

# Aprroach 3: Reversal array
# In this reversal array approach will divide the array into two chunks. The first chunks
# will be according to the number of the 'd' (that's no of times array is to be rotated ) value.   
# Reverse each part of the array and then after the reversal of the two arrays. Reverse the 
# final array with the two reversed chunks together. time complesit O(n) space complexity O(1)
"""
Algorithm:
Step 1: Define function rotaateArr.
Step 2: Create variable n to store the lenght of the array.
Step 3: Handle cases where d( no of times array should be rotated) is greater than 
size of the array. E.g if we ask to rotate by 9 times, and the size of the array is 4
in such case we're going to take the modulo..  of d respect to n. That is d = d % n
Step 4: Create a 'reverse' function whcih would be called later to reverse elements.
Step 5: Reverse 1st d elements , that's 0 --- d-1, This is used because this is an array
We will start from the first element in the array  with index positon of '0'  and end at 'd-1'
because we are picking the elements in the array that's is equivalent to the  no of 'd'
we have given for our 1st chunk.
Step 5: Reverse remaining n-d elements..
"""


