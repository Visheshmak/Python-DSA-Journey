"""
Problem: Longest Substring Without Repeating Characters
LeetCode: #3
Difficulty: Medium

Approach:
1. Use a sliding window technique to find the longest substring without repeating characters.
2. Initialize two pointers, left and right, to represent the current window.
3. Use a set to keep track of the characters in the current window.
4. Iterate through the string with the right pointer, adding the current character to the set.
5. If the current character is already in the set, move the left pointer to the right until the current character is no longer in the set, removing characters from the set as you go.


Time Complexity: O(n) where n is the length of the input string (since we are traversing the string once with the right pointer and moving the left pointer as needed)
Space Complexity: O(min(n, m)) where n is the length of the input string and m is the size of the character set (since we are using a set to store the characters in the current window)

"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = 0
        longest = 0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])

            longest = max(longest , right - left + 1)

        return longest        