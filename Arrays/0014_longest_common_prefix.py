"""
Problem: Longest Common Prefix
LeetCode: #14
Difficulty: Easy

Approach:
1. Assume the first string is the common prefix.
2. Compare the prefix with every other string.
3. If a string does not start with the current prefix,
   keep removing the last character from the prefix.
4. Repeat until all strings share the same prefix.
5. Return the final prefix.

Example:
Input: ["flower", "flow", "flight"]

prefix = "flower"
Compare with "flow"   -> prefix becomes "flow"
Compare with "flight" -> prefix becomes "fl"

Output: "fl"

Time Complexity: O(n × m)
where n = number of strings,
m = length of the shortest string

Space Complexity: O(1)
"""
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return""
        for i in range(len(strs[0])):
            char = strs[0][i]    

            for word in strs[1:]:
                if i >= len(word) or word[i] != char:
                    return strs[0][:i]
        return strs[0]            


