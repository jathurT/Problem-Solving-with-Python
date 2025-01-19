# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumb0ers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        #  Approach 1
        def get_number(node):
            number = 0
            multiplier = 1
            while node:
                number += node.val * multiplier
                multiplier *= 10
                node = node.next
            return number

        def get_linked_list(number):
            head = ListNode()
            current = head
            while number:
                current.next = ListNode(number % 10)
                number //= 10
                current = current.next
            return head.next

        number1 = get_number(l1)
        number2 = get_number(l2)
        return get_linked_list(number1 + number2)

    # Approach 2
    #     dummy = ListNode()
    #     current = dummy
    #     carry = 0
    #     while l1 or l2:
    #         sum = carry
    #         if l1:
    #             sum += l1.val
    #             l1 = l1.next
    #         if l2:
    #             sum += l2.val
    #             l2 = l2.next
    #         carry = sum // 10
    #         current.next = ListNode(sum % 10)
    #         current = current.next
    #     if carry:
    #         current.next = ListNode(carry)
    #         return dummy.next
