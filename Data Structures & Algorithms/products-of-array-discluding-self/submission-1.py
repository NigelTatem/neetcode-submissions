from collections import Counter

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
         frequencies = Counter(nums)
         total_product = 1

         if frequencies[0] >= 2:
            return [0] * len(nums)
         elif frequencies[0] == 1:
            output = [0] * len(nums)
            valid_index = nums.index(0)

            for num in nums:
                if num != 0:
                    total_product *= num
            
            output[valid_index] = total_product
         else:
            output = []
            for num in nums:
                total_product *= num
            for num in nums:
                output.append(total_product // num)
        
         return output






