"""
Problem: Richest Customer Wealth
LeetCode: #1672
Difficulty: Easy

Approach:
1. Iterate through each customer's account balances.
2. Calculate the total wealth for each customer by summing their account balances.


Time Complexity: O(m * n)
Space Complexity: O(1)
"""

from typing import List
class Soluttion:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0
        for customer in accounts:
            wealth = 0

            for money in customer:
                wealth += money

            if wealth > max_wealth:
                max_wealth = wealth

        return max_wealth