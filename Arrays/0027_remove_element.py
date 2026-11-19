"""
Problem: Remove Element
LeetCode: #27
Difficulty: Easy

Approach:
1. Use a two-pointer technique to remove the specified element in-place.
2. Initialize a pointer to keep track of the position where the next non-target element should be placed.
3. Iterate through the array with another pointer.
4. If the current element is not the target, place it at the insert position and increment the insert position.
5. Return the insert position as the new length of the array.

Time Complexity: O(n) where n is the number of elements in nums (since we are traversing the array once)
Space Complexity: O(1) since we are using a constant amount of extra space for variables (insert_position)
"""
from ast import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        insert_position = 0

        for num in nums:
            if num != val:
                nums[insert_position] = num

                insert_position += 1

        return insert_position        