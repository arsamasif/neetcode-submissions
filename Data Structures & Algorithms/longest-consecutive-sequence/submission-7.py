class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sorted_nums = sorted(set(nums))
        if not sorted_nums:
            return 0
        if len(sorted_nums) == 1:
            return 1
        print(sorted_nums)
        cached_streak = 0
        longest_streak = 1
        i, j = 0, 1
        while i < len(sorted_nums) and j < len(sorted_nums):
            if sorted_nums[i] + 1 == sorted_nums[j]:
                i += 1
                j += 1
                longest_streak += 1
            else:
                i = j
                j = i + 1
                if longest_streak > cached_streak:
                    cached_streak = longest_streak
                longest_streak = 1
        return max(longest_streak, cached_streak)