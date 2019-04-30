from collections import Counter
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max = 0
        for i in range(len(s)):
            for j in range(i, len(s) + 1):
                _s = s[i:j]
                # maxより文字列が短い場合は、探索をパスする
                if len(_s) <= max:
                    continue
                counter = Counter(_s)
                if all([counter.get(k) == 1 for k in counter]):
                    max = len(_s)
                else:
                    # この時点で重複していれば、以降は全部重複しているので探索終了
                    break
        return max
