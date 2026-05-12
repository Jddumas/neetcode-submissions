class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # sliding window. find the min and max

        min_price = float('inf')
        max_price = 0

        for price in prices:
            if price < min_price:
                min_price = price

            new_max_price = price - min_price
            max_price = max(max_price, new_max_price)

        return max_price
        