""" 
First Missing Positive Number:

nums = [3, 4, -1, 1, 2, 2, 7, 8, 0, 6, 5]
output: 9
Note: if every element is in the array from 1 to len(nums), that means we need to return the next missing positive number, which is len(nums)+1  """

"""
simple solution:

1) We first convert the list into a set so that element lookups can be done in O(1) time using hashing.
2) To find the missing positive number, we loop from 1 to n+1:
    * We start from 1 because it is the first positive integer.
    * We go up to n+1 because the second argument in the range() function is exclusive.
3) For each number in this range, we check if it is not in the set:
    * The first number not found in the set is the smallest missing positive integer.
4) If all numbers from 1 to n are present, we return n+1 as the missing number. """

def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        set1 = set(nums)

        for i in range(1,n+1):
            if i not in set1:
                return i
        return n+1
   
"""
Time: O(N)
Space: O(N) """

"""
Optimal solution 
does not preserve both the original elements and its order at end of the output list as we are modifying the input array 
"""
"""
🧠 Logic Explanation: firstMissingPositive (Constant Space)
   •	We know we need to do it in constant space, so we have to play with the input array.
   •	At worst, the array can contain numbers from 1 to n, so we cannot rely on an extra array — that would break the space constraint.

✅ Our Goal
   	* While traversing the array, we want to know which numbers are present and which number is the first missing positive.
   	* We can take advantage of the fact that the array may contain negative numbers.
      We’ll use the negative sign as an indicator that a number is present.

🔹 Step 1: Ignore Irrelevant Numbers

   •	We don’t want numbers that are less than or equal to 0 Or greater than n
   •	So we convert them to n + 1.

   This way, we don't accidentally mark wrong indices in the next step.

🔹 Step 2: Use Index as a Marker

   *	We know if a number like 3 is in the array, we should mark index 2 (i.e., 3 - 1) to indicate presence.
   *	So we go to nums[abs(nums[i]) - 1] and make it negative.
   *	But there are two things we need to be careful about:
      1.	We must only do this for numbers ≤ n
      2.	We must not flip a number back to positive if it’s already negative
   * So we multiply it like this: 
       nums[abs(nums[i]) - 1] = -1 * abs(nums[abs(nums[i]) - 1])

🔹 Step 3: Find the First Missing
   *	Finally, we loop from index 0 to n-1:
      	If we see a positive number, it means i + 1 is the missing number.
   *	If all numbers are marked (i.e., negative),
         it means 1 to n are present, so the missing number is n + 1.

✅ Why This Works
   •	We never used any extra space → truly constant space
   •	We go through the array three times, so it's O(n) time
   •	We use the input array itself to mark and track the presence of numbers using the negative sign """

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
Time: O(N)
Space: O(1) """


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

"""
Time: O(N)
Space: O(1) """
