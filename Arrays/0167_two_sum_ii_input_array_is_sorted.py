"""
Problem: Two Sum II - Input Array Is Sorted
LeetCode: #167
Difficulty: Medium

Approach:
1. Use two pointers, one starting at the beginning (left) and one at the end (right) of the sorted numbers array.
2. Calculate the sum of the elements at the two pointers.
3. If the sum equals the target, return the indices of the two numbers (1-indexed).
4. If the sum is less than the target, move the left pointer to the right to increase the sum.
5. If the sum is greater than the target, move the right pointer to the left to decrease the sum.   


Time Complexity: O(n) where n is the number of elements in the numbers array (since we are traversing the array once)
Space Complexity: O(1) since we are using a constant amount of extra space for variables (left, right, current_sum)
"""


from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            current_sum = numbers[left] + numbers[right]

            if current_sum == target:
                return[left+1 , right+1]
            elif current_sum < target:
                left += 1
            else:
                right -= 1            