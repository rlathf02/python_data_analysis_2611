
import numpy as np
print('====일반 리스트====')
a = [1,2,3]
b = [4,5,6]
print(a+b)

import sys
# 설치가 안될 시
#import sys
# 파이썬이 설치된 경로 추출

print(sys.executable)
# 터미널 : 추출한 경로 -m pip install 외부라이브러리이름

print('====numpy====')
a = np.array([1,2,3])
a = np.array([4,5,6])
print(a + b)

print('====numpy02====')
np.array([1, 2, 3, 4])
arr1 = np.array([1, 2, 3, 4])
arr2 = [1,2,3,4]

print(type(arr1))
print(type(arr2))


print('====numpy03====')
# 1차원 배열 : 숫자가 한줄로 늘어선상태
# 2차원 배열 : 숫자가 가로와 세로로 된 표 모양
# 3차원 배열 : 2차원 배열이 여러 장 겹친 입체가 된 모양

arr2 = np.array([[1,2,3,4],[5,6,7,8]])

arr3 = np.array([[[1,2,3,4],[5,6,7,8]],
[[1,2,3,4],[5,6,7,8]],[[1,2,3,4],[5,6,7,8]]])

print('2차원 배열')
print(arr2)
print('3차원 배열')
print(arr3)

print('====numpy04====')
a = np.array([1,2,3,4])

print(a+1)
print(a*2)
print(a ** 2)

print('====numpy05===')
arr1 = np.array([1,2,3,4])

arr2 = np.array([[1,2,3,4],[5,6,7,8]])

arr3 = np.array([[[0.1,0.2,0.3,0.4],[5,6,7,8]],
[[1,2,3,4],[1,2,3,4]]])

#배열의 차원수
print(arr1.ndim)
print(arr2.ndim)
print(arr3.ndim)

# shape : 배열의 형태(배열 구조를 튜플로 보여줌)
# 튜플 : 리스트와 비슷하지만 가장 큰 차이점은 한 번 생성한 튜플의 요소를 
# 수정하거나 삭제할 수 없다
# (총 개수, 행 개수, 열 개수)
print(arr1.shape) #4
print(arr2.shape)  #2 ,4 =8
print(arr3.shape)  #2 2 4 =16
#위에 결과값만 보고 싶을때는 아래처럼
print(arr1.size) 
print(arr2.size) 
print(arr3.size)  

#dtype : 배열 요소의 데이터 타입
print(arr1.dtype)
print(arr2.dtype)
print(arr3.dtype) #소수가 하나라도 껴있으면 float로 나옴

print(arr1.itemsize)
print(arr2.itemsize)
print(arr3.itemsize)

# data : 배열의 실제 데이터가 저장된 메모리 버퍼(butter 주소)
print(arr1.data)
print(arr2.data)
print(arr3.data)


print('====numpy06===')
# ndArray T : 전치 행렬(행/열을 서로 바꾸는 것)
arr = np.array([[1,2,3],[4,5,6]])
print('원래 배열')
print(arr)

print('전치 배열')
print(arr.T)

print('====numpy07===')
arr = np.array([[1,2,3],[4,5,6]])
print('원래 배열')
print(arr)

print('1차원으로 펼친 배열')
print(arr.flatten())

flat = arr.flatten()
flat[0] = 100

print('배열 출력')
print(arr)
print(flat)


print('====numpy08===') # ndArry.reshape(): 배열 모양 바꾸기-------
arr = np.array([1,2,3,4,5,6])

print('원래 배열')
print(arr)

#reshape 할 때 원본과 size가 같아야 함
arr2 = arr.reshape(2,3)
print('reshape 배열')
print(arr2)

print('====numpy09===')   #ndArray.sum() : 합계 구하기 -------------
#axis : 어느 축을 기준으로 계산할 것인가

arr = np.array([[1,2,3],
                [4,5,6]])

print('전체 합 :', arr.sum())
print('열 방향 합(axis=0):',arr.sum(axis=0))
print('행 방향 합(axis=0):',arr.sum(axis=1))


print('====numpy10===') #---------------------------평균-----

arr = np.array([[1,2,3],
                [4,5,6]])

print('전체 평균 :', arr.mean())
print('열 방향 평균(axis=0):',arr.sum(axis=0))
print('행 방향 평균(axis=0):',arr.sum(axis=1))

print('====numpy11===') #--- 최소 최댓값 구하기 ---------------------

arr = np.array([[1,2,3],
                [4,5,6]])

print('전체 최솟값 :', arr.min())
print('전체 최댓값 :', arr.max())

print('열 방향 최솟값(axis=0):',arr.min(axis=0))
print('행 방향 최댓값(axis=0):',arr.min(axis=1))

print('열 방향 최솟값(axis=0):',arr.max(axis=0))
print('행 방향 최댓값(axis=0):',arr.max(axis=1))


print('====numpy12===') # ----------
'''
1) np.zeros(shape)
- 지정한 모양으로 배열을만들고, 모든 원소를 0으로 채운다
- 주로 초기 값이 0인 배열이 필요할 때 사용(누적합, 버퍼 마스크)
- 모양은 튜플로 넣음 
'''

print(np.zeros((3,4)))

print('====numpy13===') #================================================

print(np.ones((2,3,4))) #2층이고 3행 4열이다 ======


print('====numpy14===') #==========================================
print(np.full((4,4),3)) # 모든 값을 3으로 채운 4*4 배열

print('====numpy15===') #==========================================

arr2 = np.array([[1,2,3,4],[5,6,7,8]])

print(np.zeros_like(arr2))
print(np.ones_like(arr2))
print(np.full_like(arr2, 2))

print('====numpy16==') #==========================================

print(np.random.randint(-100, 100, (2,3)))

print('====numpy16===')#============================================

np.random.seed(1)
print(np.random.randint(0,10,(2,3)))


np.random.seed(2)
print(np.random.randint(0,10,(2,3)))

print('====numpy17==')#=======================인덱싱, 슬라이싱 ====

arr1 = np.array([1,2,3,4]) 
([[1,2,3,4],[1,2,3,4,],[5,6,7,8]])

print('파이썬 기본 리스트 예시')
li = [1,2,3,4]
print(li[0])

print('1차원 배열 인덱싱')
print(arr1[0])

print('2차원 배열 인덱싱')
print(arr2[0,1])
print(arr2[1,2])

print('2차원 배열 슬라이싱') # 슬라이싱 =========================
print(arr2[1:2, 1:3])



print('1차원 배열 fancy 인덱싱')
print(arr1[[0,1,3]])


print('2차원 배열 fancy 인덱싱')
print(arr2[[0,1], [1,3]])

print(' fancy 인덱싱+슬라이싱')
print(arr2[:, [0,3]])
