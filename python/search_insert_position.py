class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0  # Initialize left pointer at the start of the array
        right = len(nums) - 1  # Initialize right pointer at the end of the array
        
        while left <= right:  # Continue until pointers overlap
            mid = left + (right - left) // 2  # Calculate mid-point to avoid overflow
            
            if nums[mid] == target:  # If the target is found, return the index
                return mid
            
            if nums[mid] < target:  # If target is greater, ignore left half
                left = mid + 1
            else:  # If target is smaller, ignore right half
                right = mid - 1
        
        return left  # If target isn't found, return the insertion position
