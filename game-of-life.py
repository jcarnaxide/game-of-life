from typing import List

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # print(f"len(m)={len(board)}")
        # print(f"len(n)={len(board[0])}")
        
        for m in range(len(board)):
            for n in range(len(board[0])):
                neighbors = 0
                # print(f"m={m}")
                # print(f"n={n}")
                # print("----")
                for x in [x for x in range(m-1, m+2) if x >= 0 and x < len(board)]:
                    for y in [y for y in range(n-1, n+2) if y >= 0 and y < len(board[0])]:
                        if(x == m and y == n):
                            continue
                        # print(f"  x={x}")
                        # print(f"  y={y}")
                        if board[x][y] in { -1, 1 }:
                            neighbors += 1
                            # print(f"increment neighbors to {neighbors}")
                        # print("----")
                if board[m][n] == 1:
                    if neighbors < 2:
                        # print("live->dead under pop")
                        board[m][n] = -1
                    elif neighbors > 3:
                        # print("live->dead over pop")
                        board[m][n] = -1
                else:
                    if neighbors == 3:
                        # print("dead->lived under pop")
                        board[m][n] = 2
        for m in range(len(board)):
            for n in range(len(board[0])):
                if board[m][n] == -1:
                    board[m][n] = 0
                elif board[m][n] == 2:
                    board[m][n] = 1
