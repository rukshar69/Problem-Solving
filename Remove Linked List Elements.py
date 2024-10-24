# https://leetcode.com/problems/remove-linked-list-elements/description/ (2 pointers)

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """
        ret_head = ListNode()
        p1 =head
        
        ret_head.next = head
        p2 = ret_head
        while p1 != None:
            if p1.val == val:
                p2.next = p1.next
            else:
                p2 = p1
            p1 = p1.next
        return ret_head.next
