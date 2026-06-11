"""
Problem: Two Sum
Difficulty: Easy

Approach:
Use a dictionary to store previously seen numbers.

Time Complexity: O(n)
Space Complexity: O(n)
"""
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}  

        for i, num in enumerate(nums):
            complement = target - num

            if complement in seen:
                return [seen[complement], i]

            seen[num] = i
