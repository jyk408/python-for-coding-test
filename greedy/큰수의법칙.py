"""
큰 수의 법칙은 다양한 수로 이루어진 배열이 있을 때 주어진 수들을 M번 더하여
가장 큰 수를 만들어내는 법칙이다. 단, 배열의 특정한 인덱스에 해당하는 수가 연속해서
K번을 초과하여 더해질 수 없는 것이 이 법칙의 특징이다.
배열의 크기 N, 숫자가 더해지는 횟수 M, 그리고 K가 주어질 때 큰 수의 법칙에 따른 결과를 출력하시오.

문제 해결 아이디어
  - 가장 큰 수와 두 번째로 큰 수만 저장
  - 가장 큰 수를 K번 더하고 두 번째로 큰 수를 한 번 더하는 연산을 반복
"""

# N, M, K를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())
# N개의 수를 공백으로 구분하여 수열 입력받기
data = list(map, int, input().split())

data.sort() # 입력받은 수 오름차순으로 정렬
first = data[n-1] # 가장 큰 수
second = data[n-2]

result = 0

while True:
    for i in range(k): # 가장 큰 수를 K번 더하기
        if m == 0:
            break
        result += first
        m -= 1
    if m == 0:
        break
    result  += second
    m -= 1 # 더할 때 마다 1씩 빼기
