# Solution 1
import re
class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        jewelsre = r'[' + J + r']+'
        jewelpattern = re.compile(jewelsre)
        jewel_list = jewelpattern.findall(S)

        result = 0
        if len(jewel_list):
            for i in jewel_list:
                result = result + len(i)
        return result
