#Difficulty: M
# Given an integer array nums where every element appears three times except for one,
# which appears exactly once. Find the single element and return it.
from os import remove


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
        my_dict = {}
        for num in nums:
            if num not in my_dict:
                my_dict[num] = 1
            else:
                my_dict[num] += 1
        for k, v in my_dict.items():
            if v == 1:
                return k


class Solution2:
    def singleNumber(self, nums):
        my_dict = {}
        for num in nums:
            if num not in my_dict:
                my_dict[num] = 1
            else:
                my_dict[num] += 1
                if my_dict[num] == 3:
                    del my_dict[num]
        return next(iter(my_dict))




if __name__ == '__main__':
    s = Solution()
    assert s.singleNumber([1,2,1,1]) == 2
    assert s.singleNumber([1,3,3,3]) == 1
    assert s.singleNumber([2]) == 2
    assert s.singleNumber([-1]) == -1
    assert s.singleNumber([-1,1,1,1,4,4,4]) == -1
    assert s.singleNumber([1,4,4,1,-1,4,1]) == -1

    print("\033[92mAll tests passed ✅\033[0m")


if __name__ == '__main__':
    x = Solution2()
    assert x.singleNumber([1,2,1,1]) == 2
    assert x.singleNumber([1,3,3,3]) == 1
    assert x.singleNumber([2]) == 2
    assert x.singleNumber([-1]) == -1
    assert x.singleNumber([-1,1,1,1,4,4,4]) == -1
    print("\033[92mAll tests passed ✅\033[0m")