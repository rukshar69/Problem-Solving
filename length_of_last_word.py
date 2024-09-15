#problem statement: https://leetcode.com/problems/length-of-last-word/description/
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s) - 1 #last index of string
        if s[n] == ' ': #if the end of string if a group of spaces, avoid it
            while s[n] == ' ':
                n -= 1
        ans = 0
        for i in range(n, -1, -1): #start from the end index where the char is non-space
            if s[i] == ' ': break #detect the boundary of the last word
            # print(s[i])
            ans += 1 #measure the length of the last word
        return ans
        
