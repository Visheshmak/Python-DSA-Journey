"""
Problem: Search Insert Position
LeetCode: #35
Difficulty: Easy

Approach:
1. Use binary search to find the position where the target should be inserted.
2. Initialize two pointers, left and right, to represent the search boundaries.
3. While left is less than or equal to right, calculate the middle index.
4. If the middle element is equal to the target, return the middle index.
5. If the middle element is less than the target, move the left pointer to the right.
6. Otherwise, move the right pointer to the left.
7. If the target is not found, return the left pointer's position as the insertion point.



Time Complexity: O(log n) where n is the number of elements in the nums array (since we are using binary search)
Space Complexity: O(1) since we are using a constant amount of extra space for variables
"""

from ast import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid

            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid -1 

        return left           