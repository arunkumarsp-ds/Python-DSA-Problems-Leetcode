"""
First Missing Positive Number:
nums = [3, 4, -1, 1, 2, 2, 7, 8, 0, 6, 5]
output: 9

Note if every elements are in the array from 1 to len(nums) that means we need to return next missing positive number which is len(nums)+1
"""


"""
simple solution:

1) We first convert the list into a set so that element lookups can be done in O(1) time using hashing.
2) To find the missing positive number, we loop from 1 to n+1:
    * We start from 1 because it is the first positive integer.
    * We go up to n+1 because the second argument in the range() function is exclusive.
3) For each number in this range, we check if it is not in the set:
    * The first number not found in the set is the smallest missing positive integer.
4) If all numbers from 1 to n are present, we return n+1 as the missing number."""

def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        set1 = set(nums)

        for i in range(1,n+1):
            if i not in set1:
                return i
        return n+1

"""
Optimal solution 
does not preserve both the original elements and its order at end as we are modifying the input array 
"""

def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        for i in range(n):
            if nums[i] <= 0:
                nums[i] = n+1
        
        for i in range(n):
            if abs(nums[i] <= n):
                nums[abs(nums[i])-1] = -1 * abs(nums[abs(nums[i])-1])
        
        for i in range(n):
            if nums[i] >0:
                return i+1
        return n+1

"""
Optimal solution 
preserves the original elements but still the order of elements will be changed at end as we are modifying the input array 
"""

def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        
        for i in range(n):
             while nums[i]>0 and nums[i] <=n and nums[i] !=  nums[nums[i]-1]:
                  correct_index = nums[i]-1
                  nums[i],nums[correct_index] = nums[correct_index],nums[i]
        
        for i in range(n):
             if nums[i] != i+1:
                  return i+1
        return n+1