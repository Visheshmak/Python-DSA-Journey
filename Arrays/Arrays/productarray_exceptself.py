"""
238. Product of Array Except Self
Difficulty: Medium
Approach:
1. Create an output array where output[i] will hold the product of all the elements to the left of index i.
2. Traverse the input array from left to right, and fill the output array with the cumulative product of the elements.
3. Traverse the input array from right to left, and multiply the output array with the cumulative product of the elements to the right of index i.  
4. Return the output array.
Example:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Time Complexity: O(n)
Space Complexity: O(1) (excluding the output array)

"""
from ast import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        answer = [1] * n

        left_product = 1

        for i in range(n):
            answer[i] = left_product
            left_product *= nums[i]

        right_product = 1

        for i in range(n-1, -1, -1):
            answer[i] *= right_product
            right_product *= nums[i]

        return answer