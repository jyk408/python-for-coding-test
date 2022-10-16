numbers = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(numbers, start, end):

    # 원소가 1개인 경우 종료
    if start >= end:
        return

    pivot = start # pivot은 첫 번째 원소
    left = start+1
    right = end
    # 배열 안에 있는 원소만큼 반복
    while left <= right:
        # 피벗보다 작은 데이터를 찾을 때 까지 반복
        while left <= end and numbers[left] <= numbers[pivot]:
            left += 1 # 오른쪽으로 한 칸 이동
        # 피벗보다 큰 데이터를 찾을 때 까지 반복
        while right > start and numbers[right] >= numbers[pivot]:
            right -= 1 # 왼쪽으로 한 칸 이동
        if left > right: # 왼쪽과 오른쪽 구간이 겹칠 경우 작은 데이터와 pivot을 교체
            numbers[right], numbers[pivot] = numbers[pivot], numbers[right]
        else:
            numbers[left], numbers[right] = numbers[right], numbers[left]
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(numbers, start, right-1)
    quick_sort(numbers, right+1, end)

quick_sort(numbers, 0, len(numbers)- 1)

