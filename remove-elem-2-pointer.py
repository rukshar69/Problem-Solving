# https://leetcode.com/problems/remove-element/description/
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        index = 0 #pointer to place non-val elem
        for i in range(len(nums)):
            if nums[i] != val:
                nums[index] = nums[i]
                index+=1
        return index
