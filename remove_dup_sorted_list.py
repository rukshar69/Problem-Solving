#problem statement: https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        current = head
        if current == None:
            return current
        while current.next != None: #till the end of list
            #if current and next vals are same 
            if current.val == current.next.val:
                current.next = current.next.next #push out the duplicate element
            else: #if not same, progress through the list
                current = current.next 
        return head
        
