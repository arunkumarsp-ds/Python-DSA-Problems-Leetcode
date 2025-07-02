"""
A string s is a subsequence of string t if the characters in the string s are present in string t in the same sequential order, without duplicates.
They don’t need to be in a continuous manner.

Example:
s = "abr" , t = "adbtr" → ✅ s is a subsequence of t
s = "rfcc" , t = "rfc" → ❌ s is not a subsequence of t because s has two c, but t has only one c. """

"""
We use the two-pointer approach to solve this.

1) We place our i pointer on s and j pointer on t.

2) When we find matching characters in both strings , we move both pointers. If not, we just move the j pointer because we are searching for the characters of s inside string t, so if we don't find a match 
   at the current position, we need to keep scanning t.

3) Fortunately, this approach automatically checks for duplicate cases.

    - When we already found the first occurrence of a character in s and moved both pointers, if the same character appears again in s, we won’t find another match in t (if it doesn’t exist), so the algorithm will
      return False.
    - As we are moving the pointers in the same direction, the sequential order is also maintained.

4) So, we know we can traverse the string s up to len(s) - 1, and the string t up to len(t) - 1.
   So we run the loop with the condition:

5) We return True when i == len(s), because when we find each matching character in both strings, we move i.
       - So if we have found all characters of s in t, i will become equal to len(s), which means we have found the full subsequence. Otherwise, we return False. """


def isSubsequence(self, s: str, t: str) -> bool:
    n1 = len(s)
    n2 = len(t)
    i = 0
    j = 0

    while i < n1 and j < n2:
        if s[i] == t[j]:
            i += 1
            j += 1
        else:
            j += 1
    if i == n1:
        return True
    else:
        return False

"""
Time: O(n2) 
Space: O(1) """
        
