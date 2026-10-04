class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        #print(counter)
        sorted_nums = sorted(counter, key=counter.get)
        #print(sorted_nums)
        return sorted_nums[-k:]