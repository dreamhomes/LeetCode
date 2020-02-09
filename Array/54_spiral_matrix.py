# -*- coding: utf-8 -*-

'''
@date: 2020-02-09

@author: dreamhomes

@description：54. 螺旋矩阵：二维矩阵按照螺旋顺序输出。
'''


def spiralOrder(matrix: list) -> list:
    if not matrix:
        return []
    # 模拟法
    r, c = len(matrix), len(matrix[0])
    spiral_order = []
    # 利用两个数组模拟行走方向: 右， 下， 左， 上
    direct_r = [0, 1, 0, -1]
    direct_c = [1, 0, -1, 0]
    i, j, di = 0, 0, 0
    for _ in range(r*c):  # while len(spiral_order)!=m*n:
        spiral_order.append(matrix[i][j])
        matrix[i][j] = 0
        next_i, next_j = i+direct_r[di], j+direct_c[di]
        if 0 <= next_i < r and 0 <= next_j < c and matrix[next_i][next_j] != 0:
            i, j = next_i, next_j
        else:
            di = (di+1) % 4
            i, j = i+direct_r[di], j+direct_c[di]
    return spiral_order

print(spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
