"""
n x m 크기의 얼음 틀이 있다. 구멍이 뚫려있는 부분은 0, 칸막이가 존재하는 부분은 1로 표시된다.
구멍이 뚫려있는 부분끼리 상, 하, 좌, 우로 붙어 있는 경우 서로 연결되어 있는 것으로 간주한다.
이때 얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크림의 개수를 구하는 프로그램을 작성하시오.

문제 해결 아이디어
  - 그래프 형태로 모델링이 가능하므로 DFS로 해결이 가능하다.
  - 특정한 지점의 주변 상, 하, 좌, 우를 살펴본 뒤에 주변 지점 중에서 값이 '0'이면서 방문하지 않는 지점(node)가 있다면 해당 지점을 방문(visit)한다
  - 방문한 지점에서 다시 상, 하, 좌, 우를 살펴보면서 방문을 다시 진행하면, 연결된 모든 지점을 방문한다.
  - 앞에 과정을 모든 노드에 반복하며 방문하지 않은 지점의 수를 센다
"""

# N, M을 공백으로 구분하여 입력받기
n, m = map(int, input().split())

# 2차원 리스트의 맵 정보 입력받기
graph = []
for i in range(n):
    row = list(map(int, input()))
    graph.append(row)

# DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
def dfs(x, y):
    # 주어진 범위에서 벗어난 경우 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        # 해당 노드 방문 처리
        graph[x][y] = 1
        # 상, 하, 좌, 우 위치도 모두 재귀적으로 호출
        dfs(x-1, y) # 좌
        dfs(x, y-1) # 하
        dfs(x+1, y) # 상
        dfs(x, y+1) # 우
        return True
    return False

# 모든 노드에 대하여
result = 0
for i in range(n):
    for j in range(m):
        # 현재 위치에서 DFS 수행
        if dfs(i, j) == True:
            result += 1

print(result)