
# using two pointer:
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
        