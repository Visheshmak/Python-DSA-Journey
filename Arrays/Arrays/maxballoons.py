"""
Problem: Maximum Number of Balloons
LeetCode: #1189
Difficulty: Easy

Approach:
1. Create a dictionary to count the occurrences of each character in the input string.
2. For the characters 'b', 'a', 'l', 'o', and '
n', calculate how many times they appear in the string. For 'l' and 'o', divide their counts by 2 since they are needed twice to form the word "balloon".
3. The maximum number of "balloon" words that can be formed is the minimum count among these characters.


Time Complexity: O(n) where n is the length of the input string (to count characters)
Space Complexity: O(1) since the dictionary will have a fixed number of keys (characters in "balloon")



"""

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = {}
        for ch in text:
            count[ch] = count.get(ch , 0) +1

            b = count.get('b', 0)
            a = count.get('a', 0)
            l = count.get('l', 0) // 2
            o = count.get('o', 0) // 2
            n = count.get('n', 0)    

        return min(b,a,l,o,n)    