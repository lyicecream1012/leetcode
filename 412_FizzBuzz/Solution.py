# Solution
class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        list_s = []
        for i in range(1,(n+1)):
            if i%3 == 0 or i%5 == 0:
                list_s.append("Fizz" * (not i%3) + "Buzz" * (not i%5))
                continue
            list_s.append(str(i))
        return list_s
