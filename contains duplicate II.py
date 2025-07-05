def containsNearbyDuplicate(self, nums, k):

    n = len(nums)
    
    for i in range(n):
        for j in range(i+1,n):
            if nums[i] == nums[j] and abs(i-j) <= k :
                return True
    return False

#optimal solution
def containsNearbyDuplicate(self, nums, k):

        n = len(nums)
        
        numbers_seen = {} # this will have the numbers and its latest index 

        for i in range(n):
            if nums[i] in numbers_seen: # we can also use for i,num in enumerate(nums) to make it easier
                if abs(i - numbers_seen[nums[i]]) <= k:
                    return True
            numbers_seen[nums[i]] = i
        return False
