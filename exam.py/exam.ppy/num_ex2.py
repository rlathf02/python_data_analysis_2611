import numpy as np
'''
1. 불리언 인덱싱(Boolean Indexing)
'''

print('===1.불리언 인덱싱(Boolean Indexing)==')
arr = np.array([10, 20, 30, 40, 50])

#조건식 확인
print(arr>25)

#25보다 큰 값만출력
print(arr[arr>25])

arr2 = np.array([[10, 20, 30],
                [40,50,60]])

print(arr2[arr2 >= 40])

print('=== 2. np.where() ===')
arr = np.array([10, 20, 30, 40, 50])

result = np.where(arr >= 30, 1, 0)
print(result)

scores = np.array([80, 20, 66, 78, 54])
result = np.where(scores >= 60, '합격', '불합격')
print(result)

#조건에 해당하는 위치 찾기
result = np.where(arr >= 30)
print(result[0])

print('=== 3. np.count_nonzero() ===') # 배열에서 0이아닌 원소 개수
arr = np.array([0,10,0,20,0,30])
print(np.count_nonzero(arr))

arr = np.array([10,0,20,30,40,50])
print(np.count_nonzero(arr >= 30))

arr=np.array([1, 2, 3, 4, 5, 6])
print(np.count_nonzero(arr & 2 == 0))



print('=== 4. np.argmax() ===') # 배열에서 최댓값이 있는 위치 반환  

arr = np.array([10, 40, 60, 80, 20])
print(arr.max())
print(arr.argmax())

arr2 = np.array([[10, 20, 70],
                [90, 20, 30]])
print(arr2.argmax())
print(arr2.argmax(axis=0))

# 행 별 최댓값의 열 인덱스
print(arr2.argmax(axis=1))
''''
2차원 배열에서 최댓값이
'''

print('=== 5. np.unravel_index() ===') # ===============

arr = np.array([[10, 20, 30],
                [40,50,60]])

index = arr.argmax()
print(index)
# 1차원인덱스를 2차원 좌표로 변환
position = np.unravel_index(index, arr.shape)
print(position)
print(arr[position])

''''
6. np.clip()
- 배열의 값을 지정한 최소, 최대 범위로 제한하는 함수
- 최솟값보다 작으면최솟값으로 변경
- 최댓값보다 크면 최댓값으로 변경
- 범위안의 값은 그대로 유지
- np.clip(배열, 최솟값, 최댓값)
'''

print('=== 6. np.clip() ===') # ===============
#최소 20 최대 100
arr = np.array([10, 40, 50, 90, 130])
result = np.clip(arr,20,100)
print(result)

# 점수가 100을 초과하지 않도록 설정
scores = np.array([70, 90, 110, 135])
result = np.clip(scores,0,100)
print(result)

''''
7. 브로드캐스팅(Boradcasting)
- 서로 다른 형태의 배열끼리 연산할 수 있도록 하는 기능
- 배열의 크기가 달라도 일정한 조건을 만족하면 연산가능
- 작은 배열을 큰 배열에 맞춰 연산하는 방식
- 실제로 배열을 복사해서 늘릴 필요는 없음
'''
print('=== 7.브로드캐스팅(Boradcasting) ===') # ===============

arr1 = np.array([1, 2, 3]) #(3, )
arr2 = np.array([[10, 20, 30],  #(2,3)
                [40, 50, 60]])  #arr1의 값이 arr2의 각 행에 적용됨

print(arr1 + arr2)




