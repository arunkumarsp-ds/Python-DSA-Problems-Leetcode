"""
Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order."""

# Brute Force Solution:
def twoSum(nums,target): 
    n = len(nums)
    for i in range(n-1):
         for j in range(i+1,n):
              if nums[i] + nums[j] == target:
                  return [i,j]

# Optimal solution using Hashing (Dictionary)
def twoSum(nums,target): 
    n = len(nums)
    dict1 = {}
    for i in range(n):
        diff = target - nums[i]
        if diff in dict1:
            return [dict1[diff],i]
        dict1[nums[i]] = i

"""
Note: we cannot use two pointers because we need to sort the array then we will lose our original indices"""