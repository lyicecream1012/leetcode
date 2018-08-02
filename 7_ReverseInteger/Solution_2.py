# Solution 2
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        str_pre = "-" if x < 0 else ""
        x = abs(x)

        result = 0
        if x/10 == 0:
            result = x
        else:
            while x !=0:
                result = result * 10 + x%10
                x = x/10
        result = int(str_pre + str(result))
        if result > 2**31-1 or result < -2**31:
            print "The reversed integer overflows."
            return 0
        return result
