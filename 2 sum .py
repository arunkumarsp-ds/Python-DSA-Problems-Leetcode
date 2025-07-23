"""
Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order."""

# Brute Force Solution:
"""
1.	We can use two loops: one for the i-th element and the inner loop for the j-th element.
2.	Basically, we try adding the numbers in all combinations, and check which combination gives the target.
3.	Once we find such a pair, we return those indices i and j. """

def twoSum(nums,target): 
    n = len(nums)
    for i in range(n-1):
         for j in range(i+1,n):
              if nums[i] + nums[j] == target:
                  return [i,j]
                  
"""
Time Complexity: O(n²)
Space Complexity: O(1) """

# Optimal solution using Hashing (Dictionary):
"""
1.	We can use hashing (dictionary) since we know there is only one valid combination.
2.	We traverse the list and, for each number, we subtract it from the target to get the other number in the pair and store it as a diff variable.
3.	We then check whether this diff (i.e., the other number) is already in the dictionary:
    -If it is, we return the indices of the current number and the stored diff.
	-If it is not, we add the current number as the key and its index as the value, because there's a chance this number might be part of the combination with a future number."""

def twoSum(nums,target): 
    n = len(nums)
    dict1 = {}
    for i in range(n):
        diff = target - nums[i]
        if diff in dict1:
            return [dict1[diff],i]
        dict1[nums[i]] = i
"""        
Time Complexity: O(n)
Space Complexity: O(n)  | Note: we cannot use two pointers because we need to sort the array then we will lose our original indices """
