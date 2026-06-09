# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        new_list = ListNode()
        new_list_head = new_list

        head1 = list1
        head2 = list2

        while head1 is not None and head2 is not None:
            if head1.val > head2.val:
                new_list.next = head2
                new_list = new_list.next
                head2 = head2.next
            else:
                new_list.next = head1
                new_list = new_list.next
                head1 = head1.next
        if head1 is None:
            new_list.next = head2

        elif head2 is None:
            new_list.next = head1
        return new_list_head.next
    
        