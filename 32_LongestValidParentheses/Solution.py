# Solution
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            print "This is an empty string!"
            return 0

        normalstrRe = r"[^()]+"
        normalstrPattern   = re.compile(normalstrRe)
        listnormalstr = normalstrPattern.findall(s)
        if len(listnormalstr):
            print "%s is not a parenthesis string." % s
            return 0

        list_unmatched = []
        str_len = len(s)
        for i in range(0,str_len):
            if s[i] == ")" and len(list_unmatched) !=0 and s[list_unmatched[-1]] == "(":
                list_unmatched.pop(-1)
            else:
                list_unmatched.append(i)
        list_unmatched.append(str_len)

        well_formec_cnt = list_unmatched[0]
        for index in range(0,len(list_unmatched)-1):
            distance = list_unmatched[index+1] - list_unmatched[index] - 1
            well_formec_cnt = distance if distance > well_formec_cnt else well_formec_cnt

        return well_formec_cnt
