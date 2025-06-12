""" 
Product of Array Except Self

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6] """

# 1) Brute Force

"""
1) First, we will create an empty array to store our result.
2) Then we will create a nested loop (an 'i' loop and a 'j' loop).
3) For every element, we want to multiply all the numbers except the one at the current index.
4) So, inside the inner loop, whenever the index is not the same (i != j), 
   we multiply the numbers at index j and store the final product in a variable.
5) After the inner loop ends, we append the product to our result array.
6) note we can assign element to list only if there are elements already in the list so dont use result[i] = product this will be list out of index"""

def productExceptSelf(self, nums: List[int]) -> List[int]:
    n= len(nums)
    result = []
    for i in range(n):
        product = 1
        for j in range(n):
            if i != j:
                product = product * nums[j]
        result.append(product)      
    return result 
    
""" Time:O(N^2)
    Space: O(N)"""


# 2) Optimal Solution:

"""
1) We can use the output array because it was told that it won't count as extra space.
2) We know that if we find the product of all the numbers to the left of our number
   and multiply it with the product of all the numbers to the right of the number, then it gives our answer to the respective index 
   Which is: output[i] = left product * right product

3) To do that, we need to have the left product of i in a left array and the right product of i in a right array.
   But that will take extra space. So, first we will store our left product in the output array itself.
  Then we will multiply the right product directly into the output array so that we can avoid using extra space.

4) For that, first we will have a left_product variable. 
   And we know that the leftmost element won't have any left product, which will just be 1.
   So we skip this in the loop and start from index 1.
   Then we simply calculate the left products and store them in output[i].

5) Similarly, we will find the right product.
   We assign a right_product variable to 1, and we know the rightmost element
   will not have any right product, so we skip it and run the loop in reversed order,
   excluding the last index.
   But this time, we directly multiply the right product in the output array itself
   because we already have the left product stored in it. """

def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1]*n 
        
        left_product = 1
        for i in range(1,n):
            left_product = left_product*nums[i-1]
            output[i] = left_product

        right_product = 1
        for i in reversed(range(n-1)): # index = (2,1,0)
            right_product = right_product*nums[i+1]
            output[i] = output[i]*right_product
        
        return output

""" Time: O(N)
    Space: O(N) if output array is accounted else O(1) """
