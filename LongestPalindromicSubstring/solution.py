class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_str = ""
        for i in range(len(s)):
            for j in range(len(s), i, -1):
                if len(longest_str) >= (j - i):
                    break
                _s = s[i:j]
                if _s == _s[::-1]:
                    longest_str = _s
                    # 長い方からチェックしているので、以降に見つかる回文はすべて対象外
                    break
        return longest_str
