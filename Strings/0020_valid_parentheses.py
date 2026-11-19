"""
Problem: Valid Parentheses
LeetCode: #20
Difficulty: Easy

Approach:
1. Initialize an empty stack to keep track of opening brackets.
2. Create a dictionary to map closing brackets to their corresponding opening brackets.
3. Iterate through each character in the input string:
   - If the character is an opening bracket, push it onto the stack.
    - If the character is a closing bracket, check if the stack is not empty and if the top of the stack matches the corresponding opening bracket. If it does, pop the top of the stack; otherwise, return False.  


Time Complexity: O(n) where n is the length of the input string (since we are traversing the string once)
Space Complexity: O(n) in the worst case when all characters are opening brackets (since we are using a stack to store them)
"""
import typing

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        pairs = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }
        for ch in s:
            if ch in "([{":
                stack.append(ch)
            else:
                if not stack:
                    return False
                if stack[-1] != pairs[ch]:
                    return False        
                stack.pop()
        return len(stack) == 0            