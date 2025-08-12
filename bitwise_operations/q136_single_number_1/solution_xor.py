from typing import List

class Solution:
    def single_number(self, nums: List[int]) -> int:
        sol = 0
        for num in nums:
            sol ^= num
        return sol