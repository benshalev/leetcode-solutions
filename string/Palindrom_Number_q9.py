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

class Solution:
    def isPalindrome(self, x):
        my_string = str(x)
        for i in range((len(my_string))//2):
            if my_string[i] != my_string[-(i+1)]:
                return False
        return True






if __name__ == '__main__':
    s = Solution()
    assert s.isPalindrome(121) == True
    assert s.isPalindrome(3) == True
    assert s.isPalindrome(11) == True
    assert s.isPalindrome(1211) == False
    assert s.isPalindrome(-121) == False
    print("\033[92mAll tests passed ✅\033[0m")