from find_two_sums import Solution
import unittest

class test_two_sums(unittest.TestCase):
    
    def test_twoSum_1(self):
        solution = Solution()
        self.assertEqual([0,1], solution.twoSum([2,7,11,15], 9))

    def test_twoSum_2(self):
        solution = Solution()
        self.assertEqual([1,2], solution.twoSum([3,2,4], 6))

    def test_twoSum_3(self):
        solution = Solution()
        self.assertEqual([0,1], solution.twoSum([3,3], 6))


if __name__ == '__main__':
    unittest.main()