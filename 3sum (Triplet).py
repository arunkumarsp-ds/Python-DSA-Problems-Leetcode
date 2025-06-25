# Brute Force Solution:

"""
1) we create three loops and check wheather our triplets gives 0 after summing up
2) then we will sort the list and convert it to tuple to add it to the set.
3) we sort the list to avoid duplicates and convert into set because list is unhashable as it is mutable
   whereas tuple is hashable as it is unmutable 
    eg: (1,2,3) != (3,2,1)
4) later we can return this in list of list using list comprehension
"""

def threeSum(self, nums: List[int]) -> List[List[int]]:
    output = set()
    n = len(nums)
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if nums[i]+nums[j]+nums[k] ==0:
                    triplet = sorted( [nums[i],nums[j],nums[k]])
                    output.add(tuple(triplet))
    return [list(triplet) for triplet in output]

"""
Time: O(n^3)
space: O(number of triplets)
"""

"""
Optimal solution:
"""
def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        output = []
        n = len(nums)

        for i in range(n-2):
            if i >0 and nums[i] == nums[i-1]:
                continue
            target = -1*(nums[i])

            j = i+1
            k = n-1

            while j<k:
                sum = nums[j] + nums[k]
                if sum == target:
                    triplet = [nums[i],nums[j],nums[k]]
                    output.append(triplet)
                    j +=1
                    k -=1

                    while j<k and nums[j] == nums[j-1]:
                        j += 1
                    while j<k and nums[k] == nums[k+1]:
                        k -= 1

                elif sum < target:
                    j += 1

                else:
                    k -= 1
        
        return output