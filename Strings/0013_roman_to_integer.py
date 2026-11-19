"""
Problem: Roman to Integer
LeetCode: #13
Difficulty: Easy

Approach:
1. Create a dictionary to map Roman numerals to their integer values.
2. Iterate through the input string and calculate the integer value based on the mapping.
3. Handle the special cases where a smaller numeral appears before a larger one (e.g., IV, IX, XL, XC, CD, CM).

Time Complexity: O(n) where n is the length of the input string (since we are traversing the string once)
Space Complexity: O(1) since the dictionary has a fixed size and we are using a

"""
class Solution:
    def romanToInt(self, s: str) -> int:

        roman = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }


        total = 0

        for i in range(len(s)):
            if i < len(s) - 1 and roman[s[i]] < roman[s[i+1]]:
                total -= roman[s[i]]

            else:
                total += roman[s[i]]      


        return total        