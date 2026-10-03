class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashy = {}
        for i, val in enumerate(nums):
            if target - val in hashy:
                return [hashy[target - val], i]
            hashy[val] = i