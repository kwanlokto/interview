import unittest
from minswaps import minSwaps


class TestMinSwaps(unittest.TestCase):

    # Basic cases
    def test_basic_balanced_pair(self):
        self.assertEqual(minSwaps("()"), 0)

    def test_basic_reversed_pair(self):
        self.assertEqual(minSwaps(")("), 1)

    # Impossible cases
    def test_impossible_single_open(self):
        self.assertEqual(minSwaps("("), -1)

    def test_impossible_single_close(self):
        self.assertEqual(minSwaps(")"), -1)

    def test_impossible_extra_open(self):
        self.assertEqual(minSwaps("(()"), -1)

    def test_impossible_extra_close(self):
        self.assertEqual(minSwaps("())"), -1)

    # Simple imbalanced cases
    def test_simple_imbalanced_1(self):
        self.assertEqual(minSwaps(")()("), 1)

    def test_simple_imbalanced_2(self):
        self.assertEqual(minSwaps("())("), 1)

    def test_simple_imbalanced_3(self):
        self.assertEqual(minSwaps("))(("), 1)

    # Multiple swaps needed
    def test_multiple_swaps_1(self):
        self.assertEqual(minSwaps(")))((("), 2)

    def test_multiple_swaps_2(self):
        self.assertEqual(minSwaps(")()()("), 1)

    def test_multiple_swaps_3(self):
        self.assertEqual(minSwaps("))))(((("), 2)

    # Already balanced
    def test_already_balanced_1(self):
        self.assertEqual(minSwaps("(())"), 0)

    def test_already_balanced_2(self):
        self.assertEqual(minSwaps("()()"), 0)

    def test_already_balanced_3(self):
        self.assertEqual(minSwaps("(()(()))"), 0)

    # Complex cases
    def test_complex_1(self):
        self.assertEqual(minSwaps("())(())("), 1)

    def test_complex_2(self):
        self.assertEqual(minSwaps(")()())(("), 1)

    def test_complex_3(self):
        self.assertEqual(minSwaps(")(()))(("), 1)

    def test_complex_4(self):
        self.assertEqual(minSwaps("))()(()("), 1)

    # Edge cases
    def test_edge_empty(self):
        self.assertEqual(minSwaps(""), 0)

    def test_edge_long_balanced(self):
        self.assertEqual(minSwaps("()()()()"), 0)

    def test_edge_many_swaps(self):
        self.assertEqual(minSwaps("))))))))(((((((("), 4)

    # Longer sequences
    def test_longer_1(self):
        self.assertEqual(minSwaps("()())()("), 1)

    def test_longer_2(self):
        self.assertEqual(minSwaps("()(()))("), 1)

    def test_longer_3(self):
        self.assertEqual(minSwaps(")))()((("), 2)


if __name__ == "__main__":
    unittest.main()
