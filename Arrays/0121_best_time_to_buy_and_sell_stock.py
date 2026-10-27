"""
Problem: Best Time to Buy and Sell Stock
LeetCode: #121
Difficulty: Easy

Approach:
1. Initialize two variables: min_price to track the minimum price seen so far and max_profit to track the maximum profit.
2. Iterate through the list of prices:
    - Update min_price if the current price is lower than min_price.
    - Calculate the profit by subtracting min_price from the current price.
    - Update max_profit if the calculated profit is greater than max_profit.



Time Complexity: O(n)
Space Complexity: O(1)
"""



from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            profit = price - min_price
            if profit > max_profit:
                max_profit = profit
        return max_profit       