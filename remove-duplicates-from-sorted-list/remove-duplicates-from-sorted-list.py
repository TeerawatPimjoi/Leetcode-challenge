# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        pointer = ListNode(0,head)
        while head!=None and head.next!=None:
            if head.val == head.next.val : 
                head.next = head.next.next
            else:
                head =head.next
        return  pointer.next
        