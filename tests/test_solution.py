from unittest import TestCase
from nose.tools import assert_raises


class TestSolution(TestCase):
    def test_insert(self):
        try:
            from run import Solution
        except ImportError:
            self.assertFalse("No class found")

        try:
            solution = Solution()
            self.assertRaises(TypeError, solution.insert, None)
            solution.insert(5)
            solution.insert(2)
            solution.insert(7)
            solution.insert(9)
            solution.insert(9)
            solution.insert(2)
            solution.insert(9)
            solution.insert(4)
            solution.insert(3)
            solution.insert(3)
            solution.insert(2)

            self.assertEqual(9, solution.max)
            self.assertEqual(2, solution.min)
            self.assertEqual(5, solution.mean)
            self.assertTrue(solution.mode in (2, 9))
        except:
            self.assertFalse("Function name should be insert")