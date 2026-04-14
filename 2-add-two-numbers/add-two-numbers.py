# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyhead = ListNode(0) # if we have this, we return dummyhead.next
        carry = 0
        curr = dummyhead # linkedlist patter with a reference head and moving pointer
        while (l1 is not None) or (l2 is not None) or (carry != 0):
            a1 = l1.val if l1 else 0
            a2 = l2.val if l2 else 0

            to_add = a1 + a2 + carry
            newnode = ListNode(to_add%10)
            dummyhead.val = to_add//10
            carry = to_add//10

            curr.next = newnode
            curr = newnode

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        return dummyhead.next





