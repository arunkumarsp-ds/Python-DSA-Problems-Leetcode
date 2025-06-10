"""
Majority Element in the list:

Input: nums = [3,2,3]
Output: 3

if an element in the list occurs more than n/2 times then it is majority element
"""


# Built in method (not recommended):

def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        for i in nums:
            if nums.count(i) > n/2:
                return i

# Time :O(N^2)
# Space :O(1)

"""
Brute Force:

1) we will create a dictionary in key we store numbers and in value we track the frequeny of those numbers so we can easily know which number occurs more than n/2 times.

"""

def majorityElement(self, nums: List[int]) -> int:
        dictionary = {}
        n = len(nums)
        for i in range(n):
            if nums[i] in dictionary:
                dictionary[nums[i]] += 1
            else:
                dictionary[nums[i]] = 1
        for num,count in dictionary.items():
            if count > n/2:
                return num

# Time: O(N)
# space: O(N)


"""
Optimal or better :

1) We use Moore’s Voting Algorithm here. The first element will be our initial candidate for the majority element, so we start the loop from the next element.

2) The logic is:

    * If the next element is the same as our candidate, we increase the count.

    * If not, we decrease the count because a different element has appeared.

    We keep doing this while traversing the array.

3) When the count becomes 0, it means that — so far — the votes for the current candidate have been matched by other elements (either           individually or combined). So it cannot be the majority element as of now, and we pick the current number as the new candidate.

    We continue this process until we finish the loop.

4) At the end, this candidate might be the majority element if it’s guaranteed.
   If not, we verify it by checking whether the candidate appears more than n/2 times. """

def majorityElement(self, nums: List[int]) -> int:
        candidate  = nums[0]
        count = 1
        n = len(nums)

        for i in range(1,n):
            if count == 0:
                candidate = nums[i]
                count = 1
            elif nums[i] == candidate:
                count += 1
            else:
               count -= 1

	return candidate
# Time :O(N)
# Space: O(1)
        