# 링크: https://leetcode.com/problems/merge-two-sorted-lists/description/
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy

        while list1 and list2:
            v1 = list1.val
            v2 = list2.val

            if v1 <= v2:
                current.next = ListNode(v1)
                list1 = list1.next
            elif v1 > v2:
                current.next = ListNode(v2)
                list2 = list2.next

            current = current.next

        if list1:
            current.next = list1
        if list2:
            current.next = list2

        return dummy.next