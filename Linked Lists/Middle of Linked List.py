# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        count = 0
        curr = head
        while curr: 
            count += 1
            curr = curr.next
        mid = count //2
        for i in range(0,mid):
            head = head.next
        
        return head