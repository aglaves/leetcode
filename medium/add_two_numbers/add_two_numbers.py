from operator import truediv
from typing import Optional
from list_node import ListNode

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        current_l1 = l1
        current_l2 = l2
        carry = 0
        result = None
        last_result = None

        while (current_l1 is not None or current_l2 is not None):
            l1_value = current_l1.val if current_l1 is not None else 0
            l2_value = current_l2.val if current_l2 is not None else 0

            unit_result = l1_value + l2_value + carry
            carry = unit_result // 10
            unit_result %= 10
            
            next_result = ListNode(unit_result, None)
            if (result is None): result = next_result
            else: last_result.next = next_result
            last_result = next_result

            if (current_l1 is not None): current_l1 = current_l1.next
            if (current_l2 is not None): current_l2 = current_l2.next
            
        if (carry > 0): last_result.next = ListNode(carry, None)

        return result
