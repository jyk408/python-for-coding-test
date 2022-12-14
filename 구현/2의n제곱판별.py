"""
정수 n이 주어졌을 때 n이 2의 거듭제곱이라면 True 아니면 False 를 반환

문제 해결 아이디어:
  - 2의 n제곱은 2진수로 표현시 1로 시작해 오른쪽에 0으로 채워지는 형태이다
  - e.g. 2^0 == 1
         2^1 == 10
         2^2 == 100
         2^3 == 1000
         2^4 == 10000
  - 따라서 각 수에서 1을 뺀수를 2진수로 나타내면 전부 1을 띈다

시간 복잡도 O(1): 한번의 수행만으로 결과 도출 가능

"""

def isPower(n):
    return n & (n-1) # &(비트연산자)는 둘 다 1일 경우에만 1이 된다.


