# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
          # Found the middle of the linked list.
        #When fast reaches at the end of the LL, then slow will be at the middle of LL
        if not head:return []
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next 
            fast = fast.next.next
        
        # Reversing the second half o fthe list
        prev, curr = None, slow.next
        while curr:
            nextn = curr.next
            curr.next=prev
            prev=curr
            curr=nextn

        slow.next = None
        # Merge the two lists
        head1, head2 = head, prev
        while head2:
            nextn = head1.next
            head1.next = head2
            head1 = head2
            head2 = nextn