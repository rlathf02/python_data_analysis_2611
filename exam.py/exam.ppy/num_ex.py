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


#=================================================

#심화문제2

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

