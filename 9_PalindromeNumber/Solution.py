# Solution
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        elif x/10 == 0:
            return True
        raw_num = x
        ans = 0
        while x!=0:
            ans = ans*10 +(x%10)
            x = x/10
        print ans
        if ans != raw_num:
            return False
        return True
