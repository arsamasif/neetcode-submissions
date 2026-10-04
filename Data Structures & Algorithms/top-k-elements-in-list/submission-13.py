class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #counter = Counter(nums)
        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
        sorted_nums = sorted(counter, key=counter.get)
        return sorted_nums[-k:]