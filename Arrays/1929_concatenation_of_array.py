class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        """
        Problem: Concatenation of Array
        LeetCode: #1929
        Difficulty: Easy

        Approach:
        1. Use list concatenation to create a new array that is the concatenation of nums with itself.

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        ans = []
        for num in nums:
            ans.append(num)
        for num in nums:
            ans.append(num)
        return ans