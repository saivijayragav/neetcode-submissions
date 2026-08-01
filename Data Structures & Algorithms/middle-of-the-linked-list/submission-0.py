# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n = 0
        node = head
        while node:
            node = node.next
            n += 1
        m = n // 2
        c = 0
        node = head
        while node:
            if c == m:
                return node
            node = node.next
            c += 1
        return -1