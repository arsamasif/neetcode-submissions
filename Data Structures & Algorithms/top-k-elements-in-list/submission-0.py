class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        counter_dict = Counter(nums)
        sorted_keys = sorted(counter_dict.items(), key=lambda items:items[1], reverse=True)
        res = []
        for i in range(k):
            res.append(sorted_keys[i][0])

        return res