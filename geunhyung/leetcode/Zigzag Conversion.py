# 링크: https://leetcode.com/problems/zigzag-conversion/
# 시간: 57ms
# 메모리: 16.69MB

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n = len(s)
        if numRows == 1 or n == 1:
            return s

        ret = ''
        for x in range(1, numRows + 1):
            idx = x - 1
            cnt = 1
            r1 = 2 * (x - 1) if x != 1 else 2 * (numRows - x)
            r2 = 2 * (numRows - x) if numRows != x else 2 * (x - 1)
            while idx < n:
                ret += s[idx]
                idx += r1 if cnt % 2 == 0 else r2
                cnt += 1
        return ret

'''
규칙을 찾으면 굉장히 쉬워지는 문제이다.
'''