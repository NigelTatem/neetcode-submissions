from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = Counter(nums)

        sorted_elements = sorted(frequencies.keys(), key=lambda x: frequencies[x], reverse=True)

        return sorted_elements[:k]