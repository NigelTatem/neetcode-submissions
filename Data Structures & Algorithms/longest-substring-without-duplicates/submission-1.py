class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # source of truth
        counts = defaultdict(int)
        l, longest = 0, 0

        for r, c in enumerate(s):
            counts[c] += 1
            while counts[c] > 1:
                counts[s[l]] -= 1
                l += 1

            longest = max(longest, r - l + 1)
        
        return longest

        