"""
Problem: Find GCD of Array
LeetCode: #1979
Difficulty: Easy

Approach:
1. Find the smallest and largest elements in the array.
2. Iterate from the smallest element down to 1 and check for the greatest common divisor (GCD) of the smallest and largest elements.        


Time Complexity: O(n) where n is the number of elements in nums (since we are traversing the array once to find the smallest and largest elements, and then iterating from the smallest element down to 1 to find the GCD)
Space Complexity: O(1) since we are using a constant amount of space to store the smallest and largest elements and the GCD
"""
from ast import List

class Solution:
    def findGCD(self, nums: List[int]) -> int:

        small = nums[0]
        large = nums[0]

        for num in nums:

            if num < small:
                small = num

            if num > large:
                large = num

        for i in range(small, 0, -1):

            if small % i == 0 and large % i == 0:
                return i