
print('===================심화문제1=============================')
import numpy as np

arr = np.array([[3, 6, 9],
                [2, 4, 8],
                [5, 7, 1]])

# 문제
# 1. arr의 shape과 ndim을 출력하시오.
print("shape:", arr.shape)
print("ndim:", arr.ndim)

# 2. 열 방향 평균을 구하시오.
print('열 방향 평균 :', arr.mean(axis=1))

# 3. 행 방향 최댓값을 구하시오.
print('행 방향 최댓값:', arr.max(axis=0))

# 4. arr을 전치행렬로 만든 후 shape을 출력하시오.
arr_T = arr.T
print("전치 shape:", arr_T.shape)

# 5. arr을 1차원으로 펼친 뒤 최솟값을 구하시오.
flat = arr.flatten()
print("flatten 최솟값:", flat.min())

# 6. arr을 (1, 9) 형태로 reshape 하시오.
reshaped = arr.reshape(1, 9)
print("reshape (1,9):")
print(reshaped)


print('===================심화문제2=============================')

import numpy as np

arr = np.array([[1.5, 2.5, 3.5, 4.5],
                [5.5, 6.5, 7.5, 8.5]])


# 1. arr의 dtype과 itemsize를 출력하시오.
print("dtype:", arr.dtype)
print("itemsize:", arr.itemsize)

# 2. axis=0 기준 합을 구하시오.
print("열 방향 합 :", arr.sum(axis=0))

# 3. axis=1 기준 평균을 구하시오.
print("행 방향 평균 :", arr.mean(axis=1))

# 4. (4,2) 형태로 reshape 하시오.
reshaped = arr.reshape(4, 2)
print("reshape (4,2):")
print(reshaped)

# 5. reshape 후 전치 shape 
print("전치 shape:", reshaped.T.shape)

# 6. flatten 후 shape
print("flatten shape:", arr.flatten().shape)

print('===================심화문제3=============================')

import numpy as np
arr = np.array([[12, 35, 48, 20],
                [55, 18, 72, 30],
                [25, 60, 15, 90]])

# 1. 배열에서 30 이상인 값만 출력해주세요.
print(arr[arr>=30])

# 2. 배열에서 50 이상인 값은 1, 50 미만인 값은 0으로 변경한 배열을 만들어주세요.
result = np.where(arr >= 50, 1, 0)
print(result)

# 3. 배열에서 40 이상인 원소가 총 몇 개인지 출력해주세요.
print(np.count_nonzero(arr >= 40))

# 4. 각 행에서 최댓값의 인덱스를 출력해주세요.
print(arr.argmax(axis=1))

# 5. 배열 전체에서 최댓값의 위치를 (행, 열) 형태로 출력해주세요.
index = arr.argmax()
position = np.unravel_index(index, arr.shape)
print(position)

# 6. 배열에서 20 미만인 값은 20으로, 70 초과인 값은 70으로 변경해주세요.
print(np.clip(arr, 20, 70))

print('===================심화문제4=============================')

import numpy as np

scores = np.array([[70, 85, 90],
                    [65, 75, 80],
                    [95, 60, 70],
                    [80, 90, 85]])

bonus = np.array([5, 10, 15])

# 1. 모든 학생의 점수에 과목별 보너스 점수를 더해주세요.
result = scores + bonus
print(result)

# 2. 보너스 점수를 더한 결과에서 100점을 초과한 점수는 100점으로 변경해주세요.
result = scores + bonus
result = np.clip(result, 0, 100)
print(result)

# 3. 변경된 점수를 기준으로 각 학생의 평균 점수를 구해주세요.
print(result.mean(axis=1))  # 행 기준

# 4. 변경된 점수를 기준으로 각 과목의 평균 점수를 구해주세요.
print(result.mean(axis=0)) # 열 기준

# 5. 변경된 점수에서 90점 이상인 데이터가 총 몇 개인지 구해주세요.
print(np.count_nonzero(result >= 90))

# 6. 변경된 점수를 기준으로총점이 가장 높은 학생의 번호를 출력해주세요.
# (학생 번호는 1번부터 시작)
total = result.sum(axis=1)
print(total.argmax() + 1)

# 7. 변경된 점수를 기준으로 각 학생의 평균이 85점 이상이면 '우수',
#    그렇지 않으면 '일반'을 출력해주세요.
avg = result.mean(axis=1)
grade = np.where(avg >= 85, '우수', '일반')
print(grade)

print('===================심화문제5=============================')

import numpy as np

np.random.seed(10)

print('1. 1부터 100까지의 정수 중에서 난수를 생성하여(4, 5) 배열을 만들고 arr에 저장해주세요.')
arr = np.random.randint(1, 101, (4, 5))
print(arr)

print('2. 생성된 배열의 차원, 형태, 원소 개수를 출력해주세요.')
print(arr.ndim)
print(arr.shape)
print(arr.size)

print('3. 첫 번째 행과 세 번째 행만 선택해서 출력해주세요.')
print(arr[[0, 2]])

print('4. 각 행의 평균을 구해주세요.')
print(arr.mean(axis=1))

print('5. 각 열의 최댓값을 구해주세요.')
print(arr.max(axis=0))


print('6. 50 이상인 값만 추출해주세요.')
print(arr[arr >= 50])

print('7. 70 이상인 원소가 몇 개인지 출력해주세요.')
print(np.count_nonzero(arr >= 70))

print('8. 60 이상이면 "합격", 60 미만이면 "불합격"인 새로운 배열을 만들어주세요.')
result = np.where(arr >= 60, '합격', '불합격')
print(result)

print('9. 전체 배열에서 최댓값의 위치를 (행, 열) 형태로 출력해주세요.')
index = arr.argmax()
position = np.unravel_index(index, arr.shape)
print(position)

print('배열의 모든 값에 10을 더한 뒤 100을 초과하는 값은 100으로 변경해주세요.')
result = np.clip(arr + 10, 0, 100)
print(result)

print('===================심화문제6=============================')

import numpy as np


print('===== 문제 1. 원하는 열 선택 및 평균 계산 =====')

arr = np.array([
    [4, 8, 2, 6],
    [7, 3, 9, 1],
    [5, 10, 12, 0]
])

# 1. 배열에서 네 번째 열과 두 번째 열을 순서대로 선택하여 새로운 배열을 만들어주세요.
# 예상 결과

result = arr[:,[3,1]]
print(result)

# [[ 6  8]
#  [ 1  3]
#  [ 0 10]]

# 2. 선택한 배열에서 각 행의 평균을 구해주세요.
result = arr.mean(axis=1)
print(result)

# 3. 선택한 배열에서 가장 큰 값을 출력해주세요.
result = arr.max(axis=1)
print(result)


print('===== 문제 2. 음수 데이터 처리 및 분류 =====')

arr = np.array([
    [-3,  5, -1, 8],
    [ 7, -4,  6, 2],
    [-2, -5,  0, 9]
])

# 1. 배열에서 음수인 데이터만 출력해주세요.
result = arr[arr < 0]
print(result)


# 2. 음수를 모두 0으로 변경한 새로운 배열을 만들어주세요.
result = np.where(arr < 0, 0, arr)
print(result)
#단, 원본 배열은 변경하지 않습니다.


# 3. 원본 배열에서 각 행마다 음수가 몇 개 있는지 출력해주세요.
counts = np.count_nonzero(arr < 0,axis=1)
print(counts)


# 4. 각 행에서 음수가 2개 이상이면 '확인', 그렇지 않으면 '정상'으로 분류해주세요.

result = np.where(counts >= 2, '합격', '정상')
print(result)



print('===== 문제 3. 점수 보정 및 우수 학생 찾기 =====')

scores = np.array([
    [75, 80, 90],
    [85, 70, 95],
    [60, 90, 80],
    [95, 85, 90]
])
bonus = np.array([5, 10, 15])

# 1. 각 학생의 점수에 과목별 보너스 점수를 더한 새로운 배열을 만들어주세요.
#    첫 번째 과목 : +5점
#    두 번째 과목 : +10점
#    세 번째 과목 : +15점
bonus = np.array([5, 10, 15])
result = scores + bonus
print(result)


# 2. 보너스 적용 후 100점을 초과하는 값은 100점으로 변경해주세요.

result = np.clip(result, 0, 100)
print(result)

# 3. 보정된 점수를 기준으로 각 학생의 평균 점수를 구해주세요.

avg = result.mean(axis=1)
print(avg)

# 4. 평균 점수가 가장 높은 학생의 번호를 출력해주세요. (학생 번호는 1번부터 시작)

best = avg.argmax() + 1
print('최고 점수 학생:', best)


# 5. 평균 점수가 90점 이상이면 '우수', 그렇지 않으면 '일반'으로 분류해주세요.

result = np.where(avg >= 90, '우수', '일반')
print(result)

print('===== 문제 4. 조건을 만족하는 행 추출 =====')

arr = np.array([
    [4, 6, 8, 2],
    [9, -1, 7, 5],
    [2, 3, 0, 4],
    [8, 10, 6, 8],
    [12, 3, -2, 7]
])

# 다음 두 조건을 모두 만족하는 행을 찾아주세요.
# 조건 1. 양수가 3개 이상일 것
# 조건 2. 행의 평균이 5 이상일 것


selected = []

for i in range(arr.shape[0]):

    # 현재 행
    row = arr[i]

    # 양수 개수
    positive = np.count_nonzero(row > 0)

    # 행의 평균
    avg = row.mean()

    # 모든 조건을 만족하는 경우
    if positive >= 3 and avg >= 5:
        selected.append(i)
# 1. 조건을 만족하는 행의 인덱스를 출력해주세요.

print(selected)


# 2. 조건을 만족하는 행만 추출해주세요.

result = arr[selected]
print(result)

# 3. 조건을 만족하는 행이 총 몇 개인지 출력해주세요.

print(len(selected))

# 힌트 : for문과 if문을 사용해도 됩니다.



print('===== 문제 5. 구역별 합계 비교 =====')


# 배열을 다음과 같이 4개의 구역으로 나눠주세요.
# [ 1  2] | [ 9 10]
# [ 3  4] | [11 12]
# --------+--------
# [ 5  6] | [13 14]
# [ 7  8] | [15 16]

# 1. 각 구역의 합계를 구해주세요.
arr = np.array([
    [1, 2, 9, 10],
    [3, 4, 11, 12],
    [5, 6, 13, 14],
    [7, 8, 15, 16]
])




# 2. 구역별 합계를 다음 형태의 2차원 배열로 만들어주세요.

a = arr[:2,:2].sum()
b = arr[:2,2:].sum()
c = arr[2:,:2].sum()
d = arr[2:,2:].sum()

result = np.array([
    [a,b],
    [c,d]
])
print(result)

# [[왼쪽 위 합계, 오른쪽 위 합계],
#  [왼쪽 아래 합계, 오른쪽 아래 합계]]



# 3. 합계가 가장 큰 구역의 위치를 (행, 열) 형태로 출력해주세요.

index = result.argmax()
position = np.unravel_index(index, result.shape)
print('최대 합계 위치:', position)


# 4. 가장 큰 합계도 출력해주세요.
# 힌트 : 반복문 없이 슬라이싱으로 해결할 수 있습니다.

print('최대 합계:', result.max())



