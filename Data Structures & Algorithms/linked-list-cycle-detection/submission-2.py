# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        fastpoint = head
        slowpoint = head

        while True:
            
            if not fastpoint or not slowpoint or not fastpoint.next:
                return False

            fastpoint = fastpoint.next
            fastpoint = fastpoint.next

            slowpoint = slowpoint.next

            if fastpoint == slowpoint:
                return True