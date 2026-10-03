class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        from collections import Counter
        if not nums:
            return False
        hashmap = Counter(nums)
        if max(hashmap.values()) > 1:
            return True
        return False