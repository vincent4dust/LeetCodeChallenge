# class Node():
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class LinkedList():
#     def __init__(self):
#         self.head = None

#     def push(self, new_data):
#         new_node = Node(new_data)
#         new_node.next = self.head
#         self.head = new_node

#     def printList(self):
#         temp = self.head
#         while(temp):
#             print(temp.data)
#             temp = temp.next

#     def append(self, new_data):
#         new_node = Node(new_data)
#         if self.head is None:
#             self.head = new_node
#             return

#         last = self.head
#         while(last.next):
#             last = last.next

#         last.next = new_node

# class Solution:
#     def addTwoNumbers(self, l1, l2):
#         l1_temp = l1.head
#         l2_temp = l2.head
#         l3 = LinkedList()
#         plusOne = False
#         while l1_temp is not None or l2_temp is not None:
#             if l1_temp is not None and l2_temp is not None:
#                 value = l1_temp.data + l2_temp.data
#                 if plusOne:
#                     value = value + 1
#                     plusOne = False
#                 if value >= 10:
#                     value = value - 10
#                     plusOne = True
#                 l3.append(value)

#                 l1_temp = l1_temp.next
#                 l2_temp = l2_temp.next
#             elif l1_temp is not None:
#                 value = l1_temp.data
#                 if plusOne:
#                     value = value + 1
#                     plusOne = False
#                 if value >= 10:
#                     value = value - 10
#                     plusOne = True
#                 l3.append(value)

#                 l1_temp = l1_temp.next
#             elif l2_temp is not None:
#                 value = l2_temp.data
#                 if plusOne:
#                     value = value + 1
#                     plusOne = False
#                 if value >= 10:
#                     value = value - 10
#                     plusOne = True
#                 l3.append(value)

#                 l2_temp= l2_temp.next
        
#         if plusOne:
#             l3.append(1)
#             plusOne = False

#         return l3


# l1 = LinkedList()
# for i in [2, 4, 3]:
#     l1.push(i)


# l2 = LinkedList()
# for j in [5, 6, 4]:
#     l2.push(j)

# solution = Solution()
# l3 = solution.addTwoNumbers(l1, l2)
# l3.printList()

class ListNode():
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# class Solution:
#     def addTwoNumbers(self, l1, l2):
#         l1_temp = l1
#         l2_temp = l2
#         l3 = ListNode(0)
#         tail = l3
#         plusOne = False
#         while l1_temp is not None or l2_temp is not None:
#             if l1_temp is not None and l2_temp is not None:
#                 value = l1_temp.val + l2_temp.val
#                 if plusOne:
#                     value = value + 1
#                     plusOne = False
#                 if value >= 10:
#                     value = value - 10
#                     plusOne = True
#                 tail.next = ListNode(value)
#                 tail = tail.next

#                 l1_temp = l1_temp.next
#                 l2_temp = l2_temp.next
#             elif l1_temp is not None:
#                 value = l1_temp.val
#                 if plusOne:
#                     value = value + 1
#                     plusOne = False
#                 if value >= 10:
#                     value = value - 10
#                     plusOne = True
#                 tail.next = ListNode(value)
#                 tail = tail.next

#                 l1_temp = l1_temp.next
#             elif l2_temp is not None:
#                 value = l2_temp.val
#                 if plusOne:
#                     value = value + 1
#                     plusOne = False
#                 if value >= 10:
#                     value = value - 10
#                     plusOne = True
#                 tail.next = ListNode(value)
#                 tail = tail.next

#                 l2_temp= l2_temp.next
        
#         if plusOne:
#             tail.next = ListNode(1)
#             tail = tail.next
#             plusOne = False

#         return l3.next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        result = ListNode(0)
        result_tail = result
        carry = 0

        while l1 or l2 or carry:
            val1 = (l1.val if l1 else 0)
            val2 = (l2.val if l2 else 0)
            carry, out = divmod(val1 + val2 + carry, 10)

            result_tail.next = ListNode(out)
            result_tail = result_tail.next

            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)
        
        return result.next

l1 = ListNode(2)
tail = l1
tail.next = ListNode(4)
tail = tail.next
tail.next = ListNode(3)
tail = tail.next

l2 = ListNode(5)
tail = l2
tail.next = ListNode(6)
tail = tail.next
tail.next = ListNode(4)
tail = tail.next

solution = Solution()
l3 = solution.addTwoNumbers(l1, l2)
while(l3):
    print(l3.val)
    l3 = l3.next