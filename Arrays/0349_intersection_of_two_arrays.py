"""
Problem: Intersection of Two Arrays
LeetCode: #349
Difficulty: Easy

Approach:
1. Use a hash map to store elements of the first array.
2. Iterate through the second array and check if each element exists in the hash map.
3. If an element exists, add it to the result and remove it from the hash map to avoid duplicates.


Time Complexity: O(n + m) where n is the number of elements in nums1 and m is the number of elements in nums2 (since we are traversing both arrays once)
Space Complexity: O(n) where n is the number of unique elements in nums1 (since we are using a hash map to store elements of nums1)
"""




from ast import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seen = {}
        result = []

        for x in nums1:
            seen[x] = 1

        for x in  nums2:
            if x in seen and seen[x] == 1:
                result.append(x)
                seen[x] = 0
        return result        