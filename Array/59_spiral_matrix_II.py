# -*- coding: utf-8 -*-

'''
@date: 2020-02-11

@author: dreamhomes

@description：59. 输出 n*n 螺旋矩阵
'''


def generateMatrix(n: int) -> list:
    # matrix = [[0]*n]*n
    matrix = [[0]*n for _ in range(n)]
    row, col = [0, 1, 0, -1], [1, 0, -1, 0]
    c_i, c_j, d_i = 0, 0, 0
    for num in range(1, n*n+1):
        matrix[c_i][c_j] = num
        next_i, next_j = c_i+row[d_i], c_j+col[d_i]
        if 0 <= next_i < n and 0 <= next_j < n and matrix[next_i][next_j] == 0:
            c_i, c_j = next_i, next_j
        else:
            d_i = (d_i+1) % 4
            c_i, c_j = c_i+row[d_i], c_j+col[d_i]

    return matrix


print(generateMatrix(3))
