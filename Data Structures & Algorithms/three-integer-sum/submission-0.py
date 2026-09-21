class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = set()
        nums.sort()
        n = len(nums)

        for i in range(n - 2):
            if nums[i] > 0:
                break
            
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            l, r = i + 1, n - 1
            while l < r:
                current_sum = nums[i] + nums[l] + nums[r]

                if current_sum == 0:
                    triplets.add((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
                elif current_sum < 0:
                    l += 1  # Sum is too small, move left pointer to increase it
                else:
                    r -= 1  # Sum is too large, move right pointer to decrease it

        # Convert the set of tuples back into a list of lists
        return [list(t) for t in triplets]




