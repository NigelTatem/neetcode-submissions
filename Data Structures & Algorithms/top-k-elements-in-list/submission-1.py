from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = Counter(nums)

        return [item for item, count in frequencies.most_common(k)]