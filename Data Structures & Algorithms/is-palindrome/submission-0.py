class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = "".join(char for char in s.lower() if char.isalnum())

        n = len(cleaned)
        l, r = 0, n - 1

        while l < r:
            if cleaned[l] == cleaned[r]:
                l += 1
                r -= 1
            else:
                return False
        
        return True

