class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for iterator_i, i in enumerate(nums):
            if target - i in hashmap:
                return [hashmap[target - i], iterator_i]
            hashmap[i] = iterator_i

