# -*- coding: utf-8 -*-

"""
@Time       : 2019/9/21 21:20
@Author     : dreamhomes
@File       : different_paths_I.py
@Description: leetcode.62 左上角到右下角的不同路径数量。
"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * n] + [[1] + [0] * (n - 1) for _ in range(m - 1)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
                # print(dp[i][j])
        return dp[-1][-1]


print(Solution.uniquePaths(None, 3, 2))
