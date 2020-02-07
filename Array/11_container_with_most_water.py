# -*- coding: utf-8 -*-

'''
@date: 2020-02-07

@author: dreamhomes

@description：leetcode 11: container with most water.
'''


def maxArea(height: list) -> int:
    max_area = 0
    length = len(height)
    # 暴力破解：O(n^2)
    # for i in range(length):
    #     for j in range(i, length):
    #         area = abs(i-j)*min(height[i], height[j])
    #         if area > max_area:
    #             max_area = area
    # 双指针：O(n)
    i, j = 0, length-1
    while i < j:
        max_area = max(max_area, (j-i)*min(height[i], height[j]))
        if height[i] > height[j]:
            j -= 1
        else:
            i += 1
        print(f'{i}-{j}-{max_area}')
    return max_area


print(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
