"""
Problem: Find Pivot Index
LeetCode: #724
Difficulty: Easy

Approach:
1. Calculate the total sum of all elements in the array.
2. Iterate through the array while maintaining a running sum of elements to the left of the current index.
3. For each index, calculate the sum of elements to the right by subtracting the left sum and the current element from the total sum.
4. If the left sum equals the right sum, return the current index as the pivot index.
5. If no pivot index is found, return -1.

Time Complexity: O(n)
Space Complexity: O(1)
"""

from ast import List
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        left_sum = 0

        for i, num in enumerate(nums):
            right_sum = total_sum - left_sum - num

            if left_sum == right_sum:
               return i
            left_sum += num

        return -1       
