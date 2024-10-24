#problem description: https://leetcode.com/problems/plus-one/description/
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = len(digits)
        remainder = 0
        for i in range(n-1, -1, -1):
            dig = digits[i]
            if i == n-1:
                dig += (1 + remainder)
            else:
                dig += remainder

            if dig >= 10:
                remainder = 1
                digits[i] = dig%10
            else:
                remainder = 0
                digits[i] = dig
        if remainder == 1:
            digits = [1] + digits
        return digits

        
