# Solution 1
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            y = 0-x
            string = str(y)
            str_new = '-'
        else:
            string = str(x)
            str_new = ''
        list_x = list(string)
        list_new = list(reversed(list_x))

        result = int(str_new + ''.join(list_new))

        if result > 2**31-1 or result < -2**31:
            print "The reversed integer overflows."
            return 0
        return result
