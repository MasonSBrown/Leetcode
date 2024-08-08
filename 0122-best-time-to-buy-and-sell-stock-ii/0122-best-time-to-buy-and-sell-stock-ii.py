class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        profit = counter = 0
        for i, v in enumerate(prices):
            if len(prices) > i+1 and v < prices[i+1]:
                profit += (prices[i+1] - v)
        return profit

        