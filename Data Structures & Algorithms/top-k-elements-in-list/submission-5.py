class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        sorted_nums = sorted(counter, key=counter.get, reverse=True)
        return sorted_nums[:k]