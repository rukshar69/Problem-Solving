# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        current_index = 0
        for i in range(1, n):
            if nums[current_index] != nums[i]:
                current_index += 1 
                nums[current_index] = nums[i]
        return current_index + 1
