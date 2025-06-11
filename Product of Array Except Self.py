# Product of Array Except Self

def productExceptSelf(self, nums: List[int]) -> List[int]:
    n= len(nums)
    result = []
    for i in range(n):
        product = 1
        for j in range(n):
            if i != j:
                product = product * nums[j]
        result.append(product) # note we can assign element to list only if there are elements already in the list 
    return result             # so dont use result[i] = product this will be list out of index