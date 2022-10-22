import sys
input = sys.stdin.readline

n, m = map(int, input().split())

board = []

for _ in range(n):
  board.append(list(input())
               
board[0][0] = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
               
queue = [[0,0]]               
               
while queue:
  x, y = queue[0][0], queue[0][1]
               
  del queue[0]
               
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]

    if nx >= 0 and ny >= 0 and nx < n and ny < m:
      if board[nx][ny]=="1":
        queue.append([nx,ny])
        board[nx][ny] = board[x][y] + 1

print(board[n-1][m-1])
