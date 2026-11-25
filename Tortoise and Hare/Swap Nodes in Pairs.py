# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        dummy = ListNode(0)
        dummy.next = head
        curr = dummy
        
        while curr.next and curr.next.next:

            slow = curr.next
            fast = curr.next.next

            curr.next = fast
            slow.next = fast.next
            fast.next = slow
            curr = curr.next.next

        return dummy.next
