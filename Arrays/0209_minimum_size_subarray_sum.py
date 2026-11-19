"""
Problem: Minimum Size Subarray Sum
LeetCode: #209
Difficulty: Medium

Approach:
1. Use a sliding window technique to find the minimum size subarray with sum at least target.
2. Initialize two pointers, left and right, to represent the current window.
3. Iterate through the array with the right pointer, adding the current element to the current sum.
4. While the current sum is greater than or equal to the target, update the minimum length and move the left pointer to the right, subtracting the leftmost element from the current sum.


Time Complexity: O(n) where n is the number of elements in nums (since we are traversing the array once with the right pointer and moving the left pointer as needed)
Space Complexity: O(1) since we are using a constant amount of extra space for variables (left, right, current_sum, min_length)
"""
from ast import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0 
        current_sum = 0
        min_length = float("inf")

        for right in range(len(nums)):
            current_sum += nums[right]
            while current_sum >= target:
                min_length = min(min_length , right - left + 1)
                current_sum -= nums[left]
                left += 1
        if min_length == float("inf"):
            return 0

        return min_length        