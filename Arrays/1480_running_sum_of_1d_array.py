"""
Problem: Running Sum of 1d Array
LeetCode: #1480
Difficulty: Easy

Approach:
1. Initialize an empty list to store the running sums and a variable to keep track of the current sum.
2. Iterate through the input list of numbers:
    - Add the current number to the current sum.
    - Append the current sum to the answer list.
3. Return the answer list containing the running sums.



Time Complexity: O(n)
Space Complexity: O(n) (for the answer list)
"""



from ast import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        answer = []
        current_sum = 0

        for num in nums:
            current_sum += num
            answer.append(current_sum)

        return answer    