"""
# This was my initial solution, then I got a faster one from chatGPT.

class Solution(object):
    def twoSum(self, nums, target):
        for index, num in enumerate(nums):
            remainder = target - num
            if remainder not in nums: continue

            second_index = nums.index(remainder)
            if second_index == index: continue

            return [index, second_index]

solution = Solution()
result = solution.twoSum([2, 7, 11, 15], 9)
print(result)
"""

class Solution(object):
    def twoSum(self, nums, target):
        seen = {}  # value -> index

        for i, num in enumerate(nums):
            remainder = target - num
            
            if remainder in seen:
                return [seen[remainder], i]
            
            seen[num] = i
