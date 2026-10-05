class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashmap = {}

        for i, val in enumerate(numbers):
            difference = target - val

            if difference in hashmap:
                return [hashmap[difference] + 1, i + 1]

            hashmap[val] = i