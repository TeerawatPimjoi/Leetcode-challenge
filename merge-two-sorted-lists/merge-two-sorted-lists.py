# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:   
        pointer = ListNode(0,None)
        ans = ListNode (0,pointer)
        while l1 != None and l2 != None:

            if l1.val < l2.val: 
                pointer.next = l1 
                l1 = l1.next 
            else: 
                pointer.next = l2
                l2 = l2.next
            pointer = pointer.next
        if l1!=None : pointer.next=l1
        if l2!=None : pointer.next=l2
        return ans.next.next

        