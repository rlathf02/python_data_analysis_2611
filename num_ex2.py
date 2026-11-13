import numpy as np

# ==========================================
# NumPy 배열 데이터 처리
# ==========================================


# 1. 불리언 인덱싱(Boolean Indexing)
# - 조건에 맞는 데이터만 추출하는 방법
# - 조건식을 적용하면 True 또는 False가 반환됨
# - True에 해당하는 데이터만 선택하여 새로운 배열 생성

arr = np.array([10, 20, 30, 40, 50])

# 조건식 확인
print(arr > 25)
# [False False True True True]

# 25보다 큰 값만 출력
print(arr[arr > 25])
# [30 40 50]

# 30 이하인 값만 출력
print(arr[arr <= 30])
# [10 20 30]

# 2차원 배열에서도 사용 가능
arr2 = np.array([[10, 20, 30],
                 [40, 50, 60]])

print(arr2[arr2 >= 40])
# [40 50 60]


# 2. np.where()
# - 조건에 따라 서로 다른 값을 선택하는 함수
# - 조건을 만족하는 데이터의 위치도 찾을 수 있음
# - np.where(조건, 참일 때 값, 거짓일 때 값)

arr = np.array([10, 20, 30, 40, 50])

# 30 이상이면 1, 아니면 0
result = np.where(arr >= 30, 1, 0)
print(result)
# [0 0 1 1 1]

# 점수가 60점 이상이면 합격, 아니면 불합격
scores = np.array([80, 45, 90, 55, 70])

result = np.where(scores >= 60, '합격', '불합격')
print(result)
# ['합격' '불합격' '합격' '불합격' '합격']

# 조건에 해당하는 위치 찾기
result = np.where(arr >= 30)
print(result[0])
# [2 3 4]


# 3. np.count_nonzero()
# - 배열에서 0이 아닌 원소의 개수를 구하는 함수
# - 조건식과 사용하면 조건을 만족하는 데이터의 개수 계산
# - True는 개수를 셀 때 1, False는 0으로 취급

arr = np.array([0, 10, 0, 20, 30, 0])

# 0이 아닌 데이터 개수
print(np.count_nonzero(arr))
# 3

# 30 이상인 데이터 개수
arr = np.array([10, 20, 30, 40, 50])

print(np.count_nonzero(arr >= 30))
# 3

# 짝수의 개수
arr = np.array([1, 2, 3, 4, 5, 6])

print(np.count_nonzero(arr % 2 == 0))
# 3


# 4. np.argmax()
# - 배열에서 최댓값이 있는 위치(인덱스)를 반환
# - 최댓값이 여러 개이면 첫 번째 위치를 반환
# - max()는 최댓값, argmax()는 최댓값의 인덱스

arr = np.array([10, 50, 20, 80, 30])

# 최댓값 출력
print(arr.max())
# 80

# 최댓값의 위치 출력
print(arr.argmax())
# 3

# 2차원 배열
arr2 = np.array([[10, 50, 20],
                 [80, 30, 40]])

# 전체 배열에서 최댓값의 인덱스
print(arr2.argmax())
# 3

# 열별 최댓값의 행 인덱스
print(arr2.argmax(axis=0))
# [1 0 1]

# 행별 최댓값의 열 인덱스
print(arr2.argmax(axis=1))
# [1 0]


# 5. np.unravel_index()
# - 1차원 인덱스를 다차원 배열의 좌표로 변환하는 함수
# - 2차원 배열에서 최댓값이 몇 행, 몇 열인지 확인할 때 사용
# - np.unravel_index(인덱스, 배열의 shape)

arr = np.array([[10, 20, 30],
                [40, 50, 60]])

# 최댓값의 인덱스 확인
index = arr.argmax()
print(index)
# 5

# 1차원 인덱스를 2차원 좌표로 변환
position = np.unravel_index(index, arr.shape)

print(position)
# (1, 2)

# 해당 좌표의 값 출력
print(arr[position])
# 60


# 6. np.clip()
# - 배열의 값을 지정한 최소, 최대 범위로 제한하는 함수
# - 최솟값보다 작으면 최솟값으로 변경
# - 최댓값보다 크면 최댓값으로 변경
# - 범위 안의 값은 그대로 유지
# - np.clip(배열, 최솟값, 최댓값)

arr = np.array([10, 30, 50, 80, 120])

# 최소 20, 최대 100으로 제한
result = np.clip(arr, 20, 100)

print(result)
# [20 30 50 80 100]

# 점수가 100점을 초과하지 않도록 설정
scores = np.array([70, 85, 105, 120])

result = np.clip(scores, 0, 100)

print(result)
# [70 85 100 100]

# 원본 배열 확인
print(scores)
# [70 85 105 120]


# 7. 브로드캐스팅(Broadcasting)
# - 서로 다른 형태의 배열끼리 연산할 수 있도록 하는 기능
# - 배열의 크기가 달라도 일정한 조건을 만족하면 연산 가능
# - 작은 배열을 큰 배열에 맞춰 연산하는 방식
# - 실제로 배열을 복사해서 늘릴 필요는 없음

# 배열과 하나의 숫자 연산
arr = np.array([10, 20, 30])

print(arr + 5)
# [15 25 35]


# 2차원 배열과 1차원 배열 연산
arr1 = np.array([[10, 20, 30],
                 [40, 50, 60]])

arr2 = np.array([1, 2, 3])

print(arr1 + arr2)
# [[11 22 33]
#  [41 52 63]]

# arr1의 shape : (2, 3)
# arr2의 shape : (3,)
# arr2의 값이 arr1의 각 행에 적용됨


# 각 과목에 보너스 점수 추가
scores = np.array([[70, 80, 90],
                   [60, 75, 85]])

bonus = np.array([5, 10, 0])

result = scores + bonus
print(result)
# [[75 90 90]
#  [65 85 85]]


# ==========================================
# 정리
# - 불리언 인덱싱 : 조건에 맞는 데이터 추출
# - np.where() : 조건에 따라 값 선택 또는 위치 확인
# - np.count_nonzero() : 0이 아닌 원소 개수 계산
# - np.argmax() : 최댓값의 인덱스 반환
# - np.unravel_index() : 1차원 인덱스를 다차원 좌표로 변환
# - np.clip() : 지정한 범위로 데이터 값 제한
# - 브로드캐스팅 : 서로 다른 형태의 배열끼리 연산
# =========================================