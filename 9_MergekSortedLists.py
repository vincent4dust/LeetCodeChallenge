"""
Given an array of k linked-lists lists, each linked-list is sorted in ascending order.
Merge all the linked-lists into one sorted linked-list and return it.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) > 0:
            list1 = lists.pop(0)
        else:
            list1 = None

        for list2 in lists:
            cur = dummy = ListNode()

            while list1 and list2:
                if list1.val < list2.val:
                    cur.next = list1
                    list1, cur = list1.next, list1
                else:
                    cur.next = list2
                    list2, cur = list2.next, list2

            if list1 or list2:
                cur.next = list1 if list1 else list2

            list1 = dummy.next

        return list1