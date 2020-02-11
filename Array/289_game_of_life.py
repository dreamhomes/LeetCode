# -*- coding: utf-8 -*-

'''
@date: 2020-02-11

@author: dreamhomes

@description：289. 生命游戏
'''


def gameOfLife(board: list) -> None:
    """
    Do not return anything, modify board in-place instead.
    """
    m, n = len(board), len(board[0])
    temp = board
    for i in range(m):
        for j in range(n):
            life = 0
            if board[i][j] == 1:
                life = life + board[i-1][j-1] if 0 <= i - \
                    1 and 0 <= j-1 else life
                life = life + board[i-1][j] if 0 <= i-1 else life
                life = life + board[i-1][j+1] if 0 <= i-1 and j+1 < n else life
                life = life + board[i][j-1] if 0 <= j-1 else life
                life = life + board[i][j+1] if j+1 < n else life
                life = life + board[i+1][j-1] if i+1 < m and 0 <= j-1 else life
                life = life + board[i+1][j] if i+1 < m else life
                life = life + board[i+1][j+1] if i+1 < m and j+1 < n else life
                if life <= 2 or life > 3:
                    temp[i][j] = 0
    pass
