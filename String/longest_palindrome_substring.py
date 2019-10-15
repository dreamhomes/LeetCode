# -*- coding: utf-8 -*-

"""
@Time       : 2019/9/25 10:11
@Author     : dreamhomes
@File       : longest_palindrome_substring.py
@Description: 给定一个字符串 s，找到 s 中最长的回文子串。回文串就是中心对称的字符串
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        def maxLenStr(left, right, ss):
            while True:
                if ss[left] == ss[right]:
                    left -= 1
                    right += 1
                else:
                    return ss[left:right]
        maxlen = 0
        for i in range(len(s)):
            l1 = maxLenStr(i, i, s)
            if maxlen < len(l1):
                maxlen = len(l1)
                maxlenstr = l1

