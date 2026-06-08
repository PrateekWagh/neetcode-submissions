# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        tempa = headA
        tempb = headB
        while tempa != tempb:
            tempa = tempa.next if tempa else headB
            tempb = tempb.next if tempb else headA
        return tempb