class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        num_set = set(nums)
        longest_sequence = 1

        for num in num_set:
            length = 1
            val = num
            if val-1 not in num_set:
                while val + 1 in num_set:
                    val += 1
                    length += 1
                    longest_sequence = max(longest_sequence, length)
        
        return longest_sequence
                