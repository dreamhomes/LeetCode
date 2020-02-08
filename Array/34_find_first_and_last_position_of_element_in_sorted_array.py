# -*- coding: utf-8 -*-

'''
@date: 2020-02-08

@author: dreamhomes

@description：34. 在有序数组中查找元素的起始位置。
'''


def searchRange(nums: list, target: int) -> list:
    if target not in nums:
        return [-1, -1]
    e = nums.index(target) + 1
    while e < len(nums) and nums[e] == target:
        e += 1
    return [nums.index(target), e-1]


print(searchRange([5, 7, 7, 8, 8, 10], 8))
