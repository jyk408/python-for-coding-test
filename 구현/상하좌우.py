"""
여행가 A는 NxN 크기의 정사각형 공간 위에 서 있다.
이 공간은 1x1크기의 정사각형으로 나 누어져 있다.
가장 왼쪽 위 좌표는 (1,1)이며, 가장 오른쪽 아래 좌표는 (N,N)에 해당한다.
여행가 A는 상 하 좌 우 방향으로 이동할 수 있으며, 시작 좌표는 항상 (1,1)이다.
우리 앞에는 여행가 A가 이동할 계획이 적힌 계획서가 놓여 있다.
계획서에는 하나의 줄에 띄어쓰기를 기준으로 하여 L, R, U, D중 하나의 문자가 반복적으로 적혀있다.
이때 여행가 A가 NxN크기의 정사각형 공간을 벗어나는 움직임은 무시된다. 예를들어 (1,1)의 위치에서 L, U를 만나면 무시된다.
다음은 N=5인 지도와 계획서이다.
계획서는 R -> R -> R -> U -> D -> D 이며 U는 공간 밖이므로 무시한다.
계획서가 주어졌을 때 여행가 A가 최종적으로 도착할 지점의 좌표를 출력하는 프로그램을 작성하시오

문제 분석:
  - 연산 횟수는 이동 횟수에 비례한다.
  - 예를들어 이동 횟수가 N인 경우 시간 복잡도는 O(N)이다.
"""

# N 입력 받기
n = int(input())
# 시작 위치 좌표
x, y = 1, 1
plans = input().split()

# L, R, U, D에 따른 이동 방향
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
move_types = ["L", "R", "U", "D"]

# 이동 계획을 하나씩 확인
for plan in plans:
    # 이동 후 좌표 구하기
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i] # x좌표 구하기
            ny = y + dy[i] # y좌표 구하기
    # 공간을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    # 위치 이동
    x, y = nx, ny

print(x, y)

