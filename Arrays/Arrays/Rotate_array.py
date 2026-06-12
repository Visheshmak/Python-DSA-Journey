
"""
Problem: Rotate Array
LeetCode: #189
Difficulty: Medium

Approach:
1. Calculate the effective rotation by taking k modulo n (length of the array).

Time Complexity: O(n)
Space Complexity: O(1)
"""
import typing

class Solution:
    def rotate(self, nums: typing.List[int], k: int) -> None:
        n = len(nums)
        k %= n
        nums[:] = nums[-k:] + nums[:-k]