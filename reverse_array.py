"""
Given an array arr[], the task is to reverse the array. Reversing an array means rearranging the elements
such that the first element becomes the last, the second element becomes second last and so on.
"""

# **APPRACH**
# They are many approach that cann be used for this, but we are going to use the best approach with the best time and space complexity.
# Since the aim is to reverse the positions of the element in the aray. (Note we are not talking about arranging then in  ascending or descending order here.)
# IDEA: The idea that we are going to  use here is simple,. We're going to create two pointers (variables) whcich will be used to initialize the left  element to the begiining and
# and the righ as well. then a 'while' loop will be used "while left<right" (obviously, we're using the position of the element not the  values ), then element at left and right
# postions, then  increase the positon of the element at the left by 1(left+=1) and decrease the position of the element right by 1 (right-=1)

# ALGORITHM:
# Step 1:Define function, and then crete two pointers "left" and "right" for holding the end and begiinning potions
# Step 2: Use a while loop, stating condition  that left < right. then swap the element at the left with right.
# Step 3: Increament left and decreament right.

def reverse_array(arr):

  # Declaring both pointer left to hold the begnning and right the end
  n = len(arr)
  left = 0
  right = n -1

  # while keeps going and stops untill condition is false, and this makes them to stop at the middle
  while left < right:
    arr[left], arr[right] = arr[right], arr[left]

    left+=1
    right-=1
# This is a dunder(special) method in functins it means the function define or called under it can only run in the current file
# It will ouput nohing when it's imported into another file.
if __name__ === "__main__":
  arr = [1, 5, 4,, 3, 9]
  reverse_array(arr)

for i in range(len(arr)):
  print(arr[i], end=" ")


    

