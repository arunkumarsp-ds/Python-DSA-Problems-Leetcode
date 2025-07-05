# bruteforce solution 
def isIsomorphic(self, s: str, t: str) -> bool:

    dict1 ={}
    n= len(s)

    for i in range(n):
        if s[i] in dict1: # if s[i] has mapped value already then i need to check
            if dict1[s[i]] != t[i]:      # if the mapped values is same has the current mapping value
                return False # if not then we are mapping another value which is prohibited
            else:
                continue     # so we have already correct mapping so we go to next char 
        else:
            if t[i] in dict1.values(): # if there is not a value mapped for this s[i] then the
                return False           # the value t[i] we are going to map should not be used for other s[i]
            else:
                dict1[s[i]] =t[i]
    return True

# optimal solution:
"""
Here we are just changing one step from above to check wheather our t character is already mapped to other
s character we use dict1.values() which is O(n) as it is similar to list so we will be using set to check it """

def isIsomorphic(self, s: str, t: str) -> bool:

    dict1 ={}
    n= len(s)

    for i in range(n):
        if s[i] in dict1: # if s[i] has mapped value already then i need to check
            if dict1[s[i]] != t[i]:      # if the mapped values is same has the current mapping value
                return False # if not then we are mapping another value which is prohibited
            else:
                continue     # so we have already have correct mapping so we go to next char 
        else:
            if t[i] in dict1.values(): # if there is not a value mapped for this s[i] then the
                return False           # the value t[i] we are going to map should not be used for other s[i]
            else:
                dict1[s[i]] =t[i]
    return True

