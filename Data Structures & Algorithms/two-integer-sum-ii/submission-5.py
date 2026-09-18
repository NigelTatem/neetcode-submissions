class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1

        while l < r:
            low, high = numbers[l], numbers[r]
            if low + high == target:
                return [l+1, r+1]
            if low + high < target:
                l+=1
            else:
                r-=1

        