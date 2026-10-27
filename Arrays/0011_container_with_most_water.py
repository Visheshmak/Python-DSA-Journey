"""
Problem: Container With Most Water
LeetCode: #11
Difficulty: Medium

Approach:
1. Use two pointers, one starting at the beginning (left) and one at the end (right) of the height array.
2. Calculate the area formed between the two pointers using the formula: area = width * min
(height[left], height[right]), where width is the distance between the two pointers.
3. Update the maximum area found so far.
4. Move the pointer pointing to the shorter line inward (either left or right) to potentially
    find a taller line that could form a larger area.


Time Complexity: O(n) where n is the number of elements in the height array (since we are traversing the array once)
Space Complexity: O(1) since we are using a constant amount of extra space for variables (left, right, max_area, width, current_height, area)
"""



from ast import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) -1
        max_area = 0

        while left < right:
            width = right - left
            current_height = min(height[left] , height[right])
            area = width * current_height
            max_area = max(max_area , area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area            