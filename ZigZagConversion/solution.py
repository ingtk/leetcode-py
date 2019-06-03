class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or len(s) <= numRows:
            return s

        block_num: int = (numRows * 2) - 2

        lst: [str] = [''] * numRows
        for i in range(len(s)):
            row: int = int(i % block_num)
            if row >= numRows:
                row = numRows - (row - numRows) - 2
            lst[row] += s[i]
        return ''.join(lst)


s = Solution()
print(s.convert('PAYPALISHIRING', 4))
