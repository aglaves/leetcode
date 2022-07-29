import unittest
from add_two_numbers import Solution
from list_node import ListNode

class add_two_numbers_test(unittest.TestCase):
    def test_add_two_numbers_1(self):
        solution = Solution()
        l1 = ListNode(2, ListNode(4, ListNode(3, None)))
        l2 = ListNode(5, ListNode(6, ListNode(4, None)))
        result = solution.addTwoNumbers(l1, l2)
        self.assertEqual(7, result.val)
        self.assertEqual(0, result.next.val)
        self.assertEqual(8, result.next.next.val)
        self.assertIsNone(result.next.next.next)

    def test_add_two_numbers_2(self):
        solution = Solution()
        l1 = ListNode(0, None)
        l2 = ListNode(0, None)
        result = solution.addTwoNumbers(l1, l2)
        self.assertEqual(0, result.val)
        self.assertIsNone(result.next)

    def test_add_two_numbers_3(self):
        solution = Solution()
        l1 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, None)))))))
        l2 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, None))))
        result = solution.addTwoNumbers(l1, l2)

        self.assertEqual(8, result.val)
        self.assertEqual(9, result.next.val)
        self.assertEqual(9, result.next.next.val)
        self.assertEqual(9, result.next.next.next.val)
        self.assertEqual(0, result.next.next.next.next.val)
        self.assertEqual(0, result.next.next.next.next.next.val)
        self.assertEqual(0, result.next.next.next.next.next.next.val)
        self.assertEqual(1, result.next.next.next.next.next.next.next.val)
        self.assertIsNone(result.next.next.next.next.next.next.next.next)

    def test_add_two_numbers_4(self):
        solution = Solution()
        l1 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, None))))
        l2 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, None)))))))
        result = solution.addTwoNumbers(l1, l2)

        self.assertEqual(8, result.val)
        self.assertEqual(9, result.next.val)
        self.assertEqual(9, result.next.next.val)
        self.assertEqual(9, result.next.next.next.val)
        self.assertEqual(0, result.next.next.next.next.val)
        self.assertEqual(0, result.next.next.next.next.next.val)
        self.assertEqual(0, result.next.next.next.next.next.next.val)
        self.assertEqual(1, result.next.next.next.next.next.next.next.val)
        self.assertIsNone(result.next.next.next.next.next.next.next.next)
    
    def test_add_two_numbers_5(self):
        solution = Solution()
        l1 = ListNode(0, ListNode(1, None))
        l2 = ListNode(0, None)
        result = solution.addTwoNumbers(l1, l2)

        self.assertEqual(0, result.val)
        self.assertEqual(1, result.next.val)
        self.assertIsNone(result.next.next)

if __name__ == '__main__':
    unittest.main()