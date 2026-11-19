"""
Problem: Contains Duplicate II
LeetCode: #219
Difficulty: Easy

Approach:
1. Use a hash map to store the indices of elements as we iterate through the array.
2. For each element, check if it has been seen before and if the difference in indices is at most k.
3. If so, return True. Otherwise, update the hash map with the current index.
4. If no such pair is found, return False.

Time Complexity: O(n) where n is the number of elements in nums (since we are traversing the array once and performing constant time operations for each element)
Space Complexity: O(n) where n is the number of unique elements in nums (since we are using a hash map to store the indices)
"""
from ast import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        seen = {}

        for i in range(len(nums)):

            if nums[i] in seen:

                if i - seen[nums[i]] <= k:
                    return True

            seen[nums[i]] = i

        return False