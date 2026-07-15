class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        i = 0
        j = 1
        while i < j and j < len(prices):
            if prices[i] > prices[j]:
                i = j
                j = j + 1
            else:
                profit = prices[j] - prices[i]
                max_profit = max(max_profit, profit)

                j = j + 1
        return max_profit

        