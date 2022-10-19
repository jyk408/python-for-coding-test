"""
2022 연세대학교 미래캠퍼스 슬기로운 코딩생활에 N명의 학생들이 응시했다.
이들 중 점수ㅏㄱ 가장 높은 k명은 상을 받을 것이다. 이 때, 상을 받는 커트라인이 몇 점인지 구하라.
커트라인이랑 상을 받는 사람들 중 점수가 가장 낮은 사람의 점수를 말한다.

제한:
  - 1<= 응시자의수(N) <= 1000   # 최대 천명의 응시자
  - 1 <= 상을받는수(K) <= N # 상을 받는 수는 응시자를 넘을 수 없다
  - 학생의 점수 최대 는 10000개
  - built-in 정렬 메소드 사용 금지

해결 아이디어:
  - 입력받는 점수 리스트를 내림차순으로 정렬
  - 점수리스트의 k번째 인덱스의 위치한 점수가 커트라인
"""

def quick_sort(scores, start, end):

    # 원소가 1개일 경우 종료
    if start >= end:
        return

    pivot = start
    left = start + 1
    right = end

    # 원소 개수 만큼 반복 (시작 인덱스가 마지막 인덱스를 넘지않을동안 반복)
    while left <= right:
        # 피벗보다 작은 데이터를 찾을 때 까지 반복 (왼쪽에서 오른쪽 방향)
        while left <= end and scores[pivot] >= scores[start]:
            left += 1
        # 피벗보다 큰 데이터를 찾을 때 까지 반복 (오른쪽에서 왼쪽 방향)
        while right > start and scores[pivot] <= scores[right]:
            right -= 1
        # 왼쪽과 오른쪽 구간이 겹칠 경우 작은 데이터와 pivot을 교체
        if left > right:
            scores[right], scores[pivot] = scores[pivot], scores[right]
        else:
            scores[right], scores[left] = scores[left], scores[right]

    # 두 파트로 분할
    quick_sort(scores, start, right-1)
    quick_sort(scores, right+1, end)

    return scores

# N, K을 공백을 기준으로 입력
# n, k = map(int, input().split())
n,k=5, 2

# 각 학생의 점수를 입력
# scores = list(map(int, input().split()))
scores = [100,76,85,93,98]

# 내림차순으로 정렬 (리스트, 시작인덱스, 마지막인덱스)
print(quick_sort(scores, 0, len(scores)-1)[-2])