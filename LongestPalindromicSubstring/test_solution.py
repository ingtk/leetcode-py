from unittest import TestCase
from solution import Solution

class TestSolution(TestCase):
    def test_lengthOfLongestSubstring(self):
        solution = Solution()
        self.assertEqual(solution.longestPalindrome("babad"), "bab")
        self.assertEqual(solution.longestPalindrome("cbbd"), "bb")
        self.assertEqual(solution.longestPalindrome("a"), "a")
        self.assertEqual(solution.longestPalindrome("ac"), "a")
