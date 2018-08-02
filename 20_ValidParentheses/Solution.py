# Solution 1
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True

        stack = []
        for i in s:
            if len(stack) != 0 and (i == ')' and stack[-1] == '(' or i == ']' and stack[-1] == '[' or i == '}' and stack[-1] == '{'):
                stack.pop(-1)
            else:
                stack.append(i)
        if len(stack) == 0:
            return True
        else:
            return False
