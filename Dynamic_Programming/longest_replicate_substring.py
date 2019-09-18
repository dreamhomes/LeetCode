# -*- coding: utf-8 -*-

"""
@Date: 2019/8/13

@Author: dreamhome

@Summary: leetcode 718. 最长重复子数组
"""


class Solution:
    def findLength(self, A: list, B: list) -> int:
        m = len(A)
        n = len(B)
        table = [[0]*(n + 1) for _ in range(m + 1)]
        # table[i][j] 表示 A[某, i-1] B[某, j-1] 的最长公共子串的长度
        # 边界条件：table[i][0] = table[0][j] = 0 因为跟空串的最长公共字串长度为 0
        # 转移方程：table[i][j] = table[i-1][j-1] + 1 if A[i-1] == B[j-1]
        #                        0                   otherwise
        '''
          ~ a p p
        ~ 0 0 0 0
        p 0 0 1 1
        p 0 0 1 2
        t 0 0 0 0
        '''
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                table[i][j] = table[i - 1][j - 1] + 1 if A[i - 1] == B[j - 1] else 0
        return max(max(row) for row in table)


print(Solution().findLength([1, 2, 3], [2, 3, 4]))
