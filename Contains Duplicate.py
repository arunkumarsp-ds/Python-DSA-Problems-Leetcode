# Given an integer array nums, return true if any value appears at least twice in the array, 
# and return false if every element is distinct.

# Optimal Solution

"""
1) we first create the set to check whether we have already visited the element or not

2) by traversing the array using loop, as soon as we visit the element:

    - if it is not already in our set, then we add it

    - if it is already there, then it means it appears two times, so we return True

3) at the end of the loop, we return False as there could be a case where we have no duplicate elements

4) we use set because we can search in O(1) time. """

def containsDuplicate(nums):
    visited = set()
    n = len(nums)
    for i in range(n):
        if nums[i] not in visited:
            visited.add(nums[i])
        else:
            return True
    return False

# Time: O(n)
# Space: O(n)
    