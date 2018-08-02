# Solution 2
class Solution(object):
   def numJewelsInStones(self, J, S):
       """
       :type J: str
       :type S: str
       :rtype: int
       """
       return sum(map(S.count, J))
