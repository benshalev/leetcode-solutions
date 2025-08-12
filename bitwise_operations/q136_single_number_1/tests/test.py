import unittest
from bitwise_operations.q136_single_number_1.solution_set import Solution as SolutionSet
from bitwise_operations.q136_single_number_1.solution_xor import Solution as SolutionXor

CASES = [
    ([2, 2, 1], 1),
    ([4, 1, 2, 1, 2], 4),
    ([1], 1),
    ([1, -2, 1], -2),
]

class TestSingleNum(unittest.TestCase):
    def test_impls(self):
        for Impl in (SolutionSet, SolutionXor):
            solver = Impl()
            for nums, expected in CASES:
                with self.subTest(impl=Impl.__name__, nums=nums):
                    self.assertEqual(solver.single_number(nums), expected)
