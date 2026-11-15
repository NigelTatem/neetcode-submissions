class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # preprocessing
        s1Count = Counter(s1)

        left = 0
        right = len(s1)
            
        while right <= len(s2):
            s2Count = Counter(s2[left:right])

            if s2Count == s1Count:
                return True

            right += 1
            left += 1
            
        return False