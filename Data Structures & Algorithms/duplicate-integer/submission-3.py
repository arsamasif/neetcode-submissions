class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique_vals = set(nums)
        if len(unique_vals) < len(nums):
            return True
        return False