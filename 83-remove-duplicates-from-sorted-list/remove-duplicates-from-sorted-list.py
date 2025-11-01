# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        current = head
        seen = set()  # to track values (like your "lists" variable)
        prev = None

        while current:
            if current.val in seen:
                # skip duplicate node
                prev.next = current.next
            else:
                seen.add(current.val)
                prev = current
            current = current.next

        return head
