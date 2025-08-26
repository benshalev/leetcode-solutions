#Difficulty: M
# Given an integer array nums where every element appears three times except for one,
# which appears exactly once. Find the single element and return it.

#You must implement a solution with a linear runtime complexity and use only constant extra space.

#Example1:
# Input: nums = [2, 2, 3, 2]
# Output: 3

# Example 2:
# Input: nums = [0, 1, 0, 1, 0, 1, 99]
# Output: 99

# Constraints:
# 1 <= nums.length <= 3 * 104
# -231 <= nums[i] <= 231 - 1
# Each
# element in nums appears exactly three times except for one element which appears once

class Solution:
    def singleNumber(self, nums):
        pos_res = 0
        neg_res = 0
        for bit in range(32):
            pos_cur = 0
            neg_cur = 0
            for n in nums:
                if n > 0 and n & (1<<bit):
                    pos_cur += 1
                if n < 0 and -n & (1<<bit):
                    neg_cur += 1
            pos_res += (pos_cur % 3) * (1 << bit)
            neg_res += (neg_cur % 3) * (1 << bit)
        return pos_res - neg_res


if __name__ == '__main':
    s = Solution()
    assert s.singleNumber([1,2,1,1]) == 2
    assert s.singleNumber([1,3,3,3]) == 1
    assert s.singleNumber([2]) == 2
    assert s.singleNumber([-1]) == -1
    assert s.singleNumber([-1,1,1,1,4,4,4]) == -1
    print("\033[92mAll tests passed ✅\033[0m")