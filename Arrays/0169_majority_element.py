"""
Problem: Majority Element
LeetCode: #169
Difficulty: Easy

Approach:
1. Use a hash map to count the occurrences of each element.
2. Iterate through the hash map and return the element with a count greater than n//2.


Time Complexity: O(n) where n is the number of elements in nums (since we are traversing the array once to count occurrences and then traversing the hash map)
Space Complexity: O(n) where n is the number of unique elements in nums (since we are using a hash map to store the counts)
"""


from ast import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}

        for num in nums:
            count[num] = count.get(num , 0) + 1
        for num in count:
            if count[num] > len(nums)//2:
                return num