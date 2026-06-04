import sys
import unittest

def assert_is_palindrome(test_case, input_str, expected):
    from main import is_palindrome
    result = is_palindrome(input_str)
    test_case.assertIsInstance(result, bool, f"is_palindrome({input_str!r}) should return a boolean")
    test_case.assertEqual(result, expected, f"is_palindrome({input_str!r}) should return {expected}")

def assert_generate_permutations(test_case, input_str, expected):
    from main import generate_permutations
    result = generate_permutations(input_str)
    test_case.assertIsInstance(result, list, f"generate_permutations({input_str!r}) should return a list")
    test_case.assertEqual(sorted(result), sorted(expected), f"generate_permutations({input_str!r}) should return {expected}")

def assert_num_paths(test_case, m, n, expected):
    from main import num_paths
    result = num_paths(m, n)
    test_case.assertIsInstance(result, int, f"num_paths({m}, {n}) should return an integer")
    test_case.assertEqual(result, expected, f"num_paths({m}, {n}) should return {expected}")

class TestRecursionPractice(unittest.TestCase):

    def test_is_palindrome(self):
        assert_is_palindrome(self, "racecar", True)
        assert_is_palindrome(self, "hello", False)
        assert_is_palindrome(self, "a", True)
        assert_is_palindrome(self, "", True)
        assert_is_palindrome(self, "madam", True)
        assert_is_palindrome(self, "palindrome", False)

    def test_generate_permutations(self):
        assert_generate_permutations(self, "abc", ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
        assert_generate_permutations(self, "", [""])
        assert_generate_permutations(self, "ab", ['ab', 'ba'])
        assert_generate_permutations(self, "a", ["a"])

    def test_num_paths(self):
        assert_num_paths(self, 2, 2, 6)
        assert_num_paths(self, 3, 3, 20)
        assert_num_paths(self, 1, 1, 2)
        assert_num_paths(self, 0, 0, 1)
        assert_num_paths(self, 2, 3, 10)
        assert_num_paths(self, 3, 2, 10)
        assert_num_paths(self, 0, 5, 1)

if __name__ == '__main__':
    unittest.main()
