class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False

        num = x
        rev = 0
        while num > 0:
            ld = num % 10
            rev = rev * 10 + ld
            num = num // 10

        return rev == x

        