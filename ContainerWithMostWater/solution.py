class Solution:

    def maxArea(self, height: [int]) -> int:
        s, e = 0, len(height) - 1
        area = -1
        while s < e:
            if height[s] >= height[e]:
                area = max(area, height[e] * (e - s))
                e -= 1
            else:
                area = max(area, height[s] * (e - s))
                s += 1
        return area

    # def maxArea(self, height: [int]) -> int:
    #     area = -1
    #     l_max = -1
    #     r_max = -1
    #     i = 0
    #     # 自分より前でコンテナができるかチェック
    #     while i < len(height):
    #         h = height[i]
    #         if l_max >= h:
    #             if h * i > area:
    #                 for b in range(0, i):
    #                     if h * (i - b) < area:
    #                         break
    #                     if height[b] < h:
    #                         continue
    #                     area = h * (i - b)
    #         else:
    #             l_max = h
    #         i += 1
    #
    #     i = len(height) - 1
    #     d = len(height) - 1
    #     # 自分よりでコンテナができるかチェック
    #     while i >= 0:
    #         h = height[i]
    #         if r_max >= h:
    #             if h * d > area:
    #                 for a in range(d, i, -1):
    #                     if h * (a - i) < area:
    #                         break
    #                     if height[a] < h:
    #                         continue
    #                     area = h * (a - i)
    #         else:
    #             r_max = h
    #         i -= 1
    #
    #     return area


s = Solution()
print(s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
print(s.maxArea([2, 1]))
print(s.maxArea(range(15000, 1, -1)))
print(s.maxArea(range(1, 15001)))
print(s.maxArea([1, 1]))
