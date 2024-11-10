# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        #find right pointer
        dummy = ListNode()
        left = dummy 
        left.next = head
        right = head
        for i in range(n):
            right = right.next
        
        while right:
            left =left.next
            right = right.next
        left.next = left.next.next
        return dummy.next
