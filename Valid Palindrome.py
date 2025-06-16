def isPalindrome(self, s: str) -> bool:
        s  = "".join(char.lower() for char in s if char.isalnum())
        n = len(s)
        for i in range(n//2):
            j = -(i+1)
            if s[i] != s[j]:
                return False
        return True