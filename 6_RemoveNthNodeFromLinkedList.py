"""
Given the head of a linked list, remove the nth node from the end of the list and return its head
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head, n):
        slow = head
        fast = head

        for i in range(n):
            if fast.next:
                fast = fast.next
            else:
                return head.next

        while (fast.next):
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

        return head