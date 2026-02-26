class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        
        for price in prices:
            # update the cheapest price so far
            if price < min_price:
                min_price = price
            # calculate profit if sold today
            elif price - min_price > max_profit:
                max_profit = price - min_price
        
        return max_profit