# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        curr = head
        l1 = []

        while curr:
            l1.append(curr.val)
            curr = curr.next

        l2 = l1[::-1]

        if l1 == l2:
            return True
        else:
            return False