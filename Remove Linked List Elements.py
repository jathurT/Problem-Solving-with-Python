# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """
        list_node = ListNode(0)
        list_node.next = head
        current = list_node
        while current.next:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next
        return list_node.next
