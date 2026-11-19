"""
Problem: Contains Duplicate
LeetCode: #217
Difficulty: Easy

Approach:
1. Use a set to keep track of elements we have seen.
2. Iterate through the array:
    - If an element is already in the set, return True (duplicate found).
    - Otherwise, add the element to the set.
3. If we finish iterating without finding duplicates, return False.

Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False        