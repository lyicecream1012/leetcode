# Solution
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if 0 in nums:
            zero = nums.index(0)  # records the position of "0"
            for i in xrange(zero+1,len(nums)):
                if nums[i] != 0:
                    nums[i], nums[zero] = nums[zero], nums[i]
                    zero += 1
