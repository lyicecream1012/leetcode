# Solution
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict_roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        result = 0
        for i in range(0,len(s)-1):
            if dict_roman[s[i]] < dict_roman[s[i+1]]:
                result = result - dict_roman[s[i]]
            else:
                result = result + dict_roman[s[i]]
        result = result + dict_roman[s[-1]]
        return result
