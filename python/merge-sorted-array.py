#prb statement: https://leetcode.com/problems/merge-sorted-array/

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        if n == 0: return
        if m == 0:
            for i in range(len(nums2)):
                nums1[i] = nums2[i]
            return
        
        i,j,res_index = m-1, n-1, m+n-1
        while i>=0 and j>=0: #fill from the last
            if nums1[i] >= nums2[j]:
                nums1[res_index] = nums1[i]
                i-=1; res_index -=1
            else:
                nums1[res_index] = nums2[j]
                j-=1; res_index -=1
        
        if j>=0: #if second array has some elements left
            while j>=0:
                nums1[res_index] = nums2[j]
                j-=1; res_index -=1
        #if first array has some elements left to be traversed they are already in place
        
