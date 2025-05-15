# Questions:

# Given an array of positive integers arr[], return the second largest element from the array. 
# If the second largest element doesn't exist then return -1.
# Note: The second largest element should not be equal to the largest element.


# **ALG/PROBLEM SOLVING APPROACH**
#  ---> First I will  check for the constraint cases,
#         Step 1: If length of array is less than 2, RETURN -1
        
#       ---> CORE LOGIC
#         Step 2: Create a placeholder(variable) to store largest value found so far..
#         It's being initialized to negative infinity ... 
        
#         Step 3: Create a placeholder(variable) to store second largest number  largest value found so far..
#         It's being initialized to negative infinity as well... 
        
#         Step 4: Iterate through the array and update the vaue of the largets and 
#         second_largest value according to the current num value.
#         i.e IF num > largest THEN num = largets ; second_largest = largest
#         ELSE IF num > second_lagest and num !=largest THEN  second_largest = num.
        
        
#         Step 5: Check for edge cases, after the ilterion and the second_largest
#         remains negative infinity, I will return -1, It means they is no largets element.
#         ELSE I will return the second_largest value
        
#         I will loop through the array with num, and keep create a variable largest
#         and second_largest. In the iteration 
        
#         **Key note**
#         1. Both largest and second_largest are initialized to negative infinity
#         "-inf" because that's the smallest possible number, because any number in
#         array would be greater than this current values and they can be easily updated
        
#         2. Reaseons why negative infinity (-inf) works:
#         .. It's a sentinel value i.e "it is not found yet"
#         .. Due to this, It guarantees only  value in the array can override it
#            unlike what happens when other value e.g "0" or other smaller value
#             are being used for the initialization
#          3. Take note of the order you update your largets and second_largets value.
#             Don't update largest before updating second_largets, rather it should be in the other way round.

   def getSecondLargest(self, arr):
        
        if len(arr) < 2:
            return -1
            
        largest = float("-inf")
        second_largest = float("-inf")
        
        for num in arr:
            if num > largest:
                second_largest = largest
                largest = num
            elif num > second_largest and num != largest:
                second_largest = num
    
        if second_largest == float("-inf"):
            return -1
        return second_largest





        
