from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, v1 in enumerate(nums):
            for j, v2 in enumerate(nums[i+1:]):
                if v1 + v2 == target:
                    return [i, i+1+j]
        return []

print(Solution().twoSum([3, 2, 4], 6))
print(Solution().twoSum([2,7,11,15], 18))
print(Solution().twoSum([3,3], 6))
