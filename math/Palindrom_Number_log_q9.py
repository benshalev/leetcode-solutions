# Given an integer x, return true if x is a palindrome, and false otherwise.
# Example 1:
# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.

# Example 2:
# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

# Example 3:
# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
import math
class Solution:
    def isPalindrome(self, x):
        if x < 0:
            return False
        if x < 10:
            return True
        div = 10 ** int(math.log10(x))
        while x:
            left = x // div
            right = x%10
            if left != right:
                return False
            x = (x % div) // 10
            div = div // 100
        return True






if __name__ == '__main__':
    s = Solution()
    assert s.isPalindrome(121) == True
    assert s.isPalindrome(3) == True
    assert s.isPalindrome(11) == True
    assert s.isPalindrome(1211) == False
    assert s.isPalindrome(-121) == False
    print("\033[92mAll tests passed ✅\033[0m")