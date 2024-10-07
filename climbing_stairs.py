#https://leetcode.com/problems/climbing-stairs/submissions/1414888368/
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        step_count = [0]*(n+1)
        step_count[0] = 1 #at the base
        step_count[1] = 1 #step 1
        if n==1: return 1
        for i in range(2,n+1):
            #step count at i is sum of step count i-1(1 step to i)
            # and step count at i-2(2 step to i)
            step_count[i] =step_count[i-1] + step_count[i-2] #dp 
        
        return step_count[n]
        
