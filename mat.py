import matplotlib.pyplot as plt
# Matplotlib : 데이터를 표현할 수 있게 해주는 파이썬 라이브러리
# figure => 큰 도화지
# subplots => 도화지 윈에 나눠진 작은 칸들

# 기본 스타일 적용
plt.style.use('default')

# y값만 전달, x는 자동으로 0, 1, 2, 3이 설정
# plt.plot([2, 4, 6, 8])

# x, y값 직접 설정
x = [2, 4, 6, 8]
y = [1, 3, 5, 7]
plt.plot(x, y)
# plt.show()

# =======================
fig = plt.figure()

# (행 개수, 열 개수, 위치값)
fig.add_subplot(1, 2, 1)
fig.add_subplot(1, 2, 2)
# plt.show()


# =======================
fig = plt.figure()

# (행 개수, 열 개수, 위치값)
fig.add_subplot(1, 3, 1)
fig.add_subplot(1, 3, 3)
# plt.show()


# =======================
fig = plt.figure()

# (행 개수, 열 개수, 위치값)
fig.add_subplot(1, 2, 1)
fig.add_subplot(2, 2, 2)
# plt.show()


# =======================
# 이전 figure 모두 닫기
plt.close('all')

fig = plt.figure()

a1 = fig.add_subplot(1, 2, 1)
a2 = fig.add_subplot(1, 2, 2)

x = range(0, 10)
y = range(5, 15)
a1.plot(x, y, 'c*')

x = range(0, 50)
y = range(0, 50)
a2.plot(x, y, 'mp')

# plt.show()


# =======================
# 이전 figure 모두 닫기
plt.close('all')

fig = plt.figure()

# ggplot 특징
# - 배경에 격자(grid)가 있음
# - 색감이 부드럽고 깔끔
# - 데이터 비교가 쉽다
plt.style.use('ggplot')

# 1행 1열짜리 영역에서 1번째 위치에 그래프 생성
a = fig.add_subplot(111)
x = [3, 4] # 막대의 위치(좌표 기준)
y = [1, 2] # 막대의 높이(값 기준)

# x축 라벨 이름(tick 이름)
labels = ['english', 'math']

# 각 막대에 적용할 색상
colors = ['red', 'blue']

# 세로 막대
# a.bar(x, y, tick_label=labels, color=colors)

#가로 막대
a.barh(x, y, tick_label=labels, color=colors)
plt.show()
















