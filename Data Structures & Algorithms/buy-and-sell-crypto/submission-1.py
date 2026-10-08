class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        
        l, r = 0, 1
        while l < len(prices) - 1:
            print(l)
            print(r)
            res = max(prices[r] - prices[l], res)
            if r == len(prices) - 1:
                l += 1
                r = l
            r += 1

        return res