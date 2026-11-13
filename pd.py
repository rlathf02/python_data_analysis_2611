import pandas as pd

df = pd.DataFrame(
    {
        "Name": [
            "Braund, Mr. Owen Harris",
            "Allen, Mr. William Henry",
            "Bonnell, Miss Elizabeth",
        ],
        "Age": [22, 35, 58],
        "Sex": ["male", "male", "female"],
    }
)

print('=== 전체 출력 ===')
print(df)


print('\n=== 열 하나씩 출력 ===')
# 결과는 DataFrame이 아니라, 'Series'라는 1차원 자료구조로 나옴
print(df['Name'])
print(df['Age'])
print(df['Sex'])


print('\n=== 타입 출력 ===')
print(type(df))
print(type(df['Age']))


print('\n=== 이름이 Age인 Series 생성 ===')
ages = pd.Series([22, 35, 44], name='Age')
print(ages)


print('\n=== DataFrame에서 특정 열 꺼내기 ===')
print(df['Age'])


print('\n=== 기본 통계 함수 ===')
print('max : 최댓값')
print('최대 나이 : ', df['Age'].max())

print('min : 최솟값')
print('최소 나이 : ', df['Age'].min())

print('mean : 평균값')
print('평균 나이 : ', df['Age'].mean())

print('요약 통계 정보 보기')
# describe : 숫자형 열에 대해 '요약 통계 정보'를 한 번에 보여줌
print(df.describe())
'''
count   3.000000 : 데이터 개수
mean   38.333333 : 평균
std    18.230012 : 표준 편차(데이터가 평균에서 얼마나 퍼져 있는지)
min    22.000000 : 최솟값
25%    28.500000 : 1사분위수(Q1)
50%    35.000000 : 중앙값(median)
75%    46.500000 : 3사분위수(Q3)
max    58.000000 : 최댓값
'''

print('DataFrame의 전체 요약 정보')
# info : DataFrame의 '구조 정보'를 보여줌
print(df.info())


print(' DataFrame는 방법 2가지==')

print(df.iloc[0])
print(df.iloc[1])
print(df.iloc[2])

print(df.loc[0])
print(df.iloc[0])

print('상위 하위 데이터 출력')
print(df.head()) #기본적으로 상위 5개 #######################
print(df.head(2)) # 두개만 볼수잇음 # 하지만 5개 미만이면 있는만큼 출력

print(df.tail(2)) #아래에서 부터 2개 출력 #######################

print('===열 수정===')

df['Survived']=[0,1,1]
print(df)

df = df.rename(columns={'Sex' : 'Gender'})
print(df)

df = df.drop('Survived', axis=1)
print(df)

print('===결측치 처리 ===') #None처리############========================

print(df)
print(df.isnull())

df2 = df.copy()

df2.loc[1, 'Age'] = None
print(df2.isnull())

print(df2.dropna(axis=0)) # 결측치가 있는 부분 제거
print(df2.fillna(0))  # 결측치를 i 값으로 채우기

print(df2['Age'].fillna(df['Age'].mean))#결측치를 평균값으로 채우기

print(df2.fillna(method='ffill'))
print(df2.ffill())
    















