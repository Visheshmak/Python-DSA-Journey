"""
Problem: Remove Duplicates from Sorted Array
LeetCode: #26
Difficulty: Easy

Approach:
1. Use two pointers to keep track of the current position in the array and the position of the last unique element.
2. Iterate through the array, and whenever a new unique element is found, move it to


Time Complexity: O(n)
Space Complexity: O(1)
"""



from ast import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[k-1]:
                nums[k] = nums[i]
                k += 1
        return k