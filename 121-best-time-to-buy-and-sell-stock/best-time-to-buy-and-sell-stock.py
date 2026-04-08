class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # just need to maintain min_price and max_profit
        # then go from left to right as shorted chronologically
        i = 0 # buy date
        profit = 0
        min_price = float('inf')
        max_profit = 0
        for p in prices:
            min_price = min(min_price,p)
            max_profit = max(max_profit, p - min_price)
        return max_profit
            