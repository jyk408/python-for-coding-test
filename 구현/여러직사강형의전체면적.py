"""
밑변이 모두 x축에 평행한 N개의 직사각형이 주어질 때, 이 N개의 직사각형들이 차지하는 면적을 구하는 프로그램을 작성하시오

"""

def area(boxes):
    # 중복 값 허용 안하기 위한 set사용
    coordinates = set([])

    for x1, y1, x2, y2 in boxes:
        for x in range(x1, x2):
            for y in range(y1, y2):
                coordinates.add((x, y))

    return len(coordinates)


boxes = [[0, 0, 200, 200]] * 4
print(area(boxes))

boxes = [[1, 2, 4, 4], [2, 3, 5, 7],
         [3, 1, 6, 5], [7, 3, 8, 6]]
print(area(boxes))