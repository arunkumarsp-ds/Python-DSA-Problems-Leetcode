"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true

Example 2:

Input: s = "rat", t = "car"
Output: false 
"""
"""
🔹 Logic:
A string t is an anagram of string s if all characters in s appear in t with the same frequency.

1) Method 1: Sorting Approach:

* To check this, we sort both strings and compare them.
    - If both sorted strings are exactly the same, then t is an anagram of s
    - Otherwise, it's not. """

def isAnagram(s,t):
        if sorted(s) == sorted(t): # sorted(string) will result into list
            return True
        else:
            return False

"""
Time: O(n log n) → due to sorting both strings (each of length n)
Space : O(n) as sorted() will create list """

"""
2) Method 2: Frequency Count (Optimal):

1) we know if the frequency of the characters is same then it is anagram.

2) so we need to store the frequency of the characters and need to compare — if both are same then it is anagram.

3) to do that we can use list [0]*26 — essentially it will have 26 -0's in it as we have 26 alphabets.

4) so whenever we see the character we will increment the count.

5) to correctly update the count for the respective character we use ord() function. 

	-  when we see char = a then our index should be 0 , so ord(char) - ord(a) will give correct index for all alphabets. """

def isAnagram(s,t):
    if len(s) != len(t):
        return False

    n = len(s)
    count_t = [0] *26
    count_s = [0] *26

    for i in range(n):
        count_t[ord(t[i]) -ord("a")] += 1
        count_s[ord(s[i]) -ord("a")] += 1

    if count_t == count_s:
        return True
    else:
        return False
    
"""
Time: O(n)
Space: O(1) → space is constant irrespective of the string size, it is always going to be 26 """

"""

3) alternate method for 2nd method instead of counting the frequency manually using list we can use Counter:

	- eg: if s = "batting" then Counter(s) will result as Counter({'t': 2, 'b': 1, 'a': 1, 'i': 1, 'n': 1, 'g': 1}) """

from collections import Counter

def isAnagram(s, t):
    return Counter(s) == Counter(t)

"""
Time: O(n)
Space: O(n) or O(1) in theory it uses extra space for the dictionaries, but since we only deal with lowercase letters it is still considered constant """
