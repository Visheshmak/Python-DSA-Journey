"""
Problem: Find First Occurrence of String
LeetCode: #28
Difficulty: Easy

Approach:
1. Iterate through the haystack string and check for the needle string at each position.
2. If a match is found, return the index of the first occurrence.



Time Complexity: O(n*m) where n is the length of haystack and m is the length of needle (since we are traversing the haystack and checking for the needle at each position)
Space Complexity: O(1) since we are using a constant amount of space to store the index of the first occurrence
"""
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)- len(needle) + 1):
            match = True

            for j in range(len(needle)):

                if haystack[i+j] != needle[j]:
                    match = False
                    break

            if match:
                return i
        return -1            