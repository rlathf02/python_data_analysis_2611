from openpyxl import *
from openpyxl.chart import BarChart, Reference

# == 차트 만들기 ==

wb = Workbook()
ws = wb.active

# 예제 데이터 입력
ws.append(['Name', 'Score']) # 헤더 행
ws.append(['홍길동', 90])
ws.append(['홍길순', 80])
ws.append(['임꺽정', 70])

# BarChart 객체 생성(막대 그래프)
chart = BarChart()

# 차트에 사용할 데이터 범위 지정
# min_col=2 -> B열(Score)
# min_row=1 -> 1행부터
# max_row=5 -> 5행까지
data = Reference(ws, min_col=2, min_row=1, max_row=5)

# 지정한 데이터를 차트에 추가
# 첫 행을 Series name(계열 이름)으로 사용
chart.add_data(data, titles_from_data=True)

# 차트 제목 설정
chart.title = 'Student Scores'

# 차트를 워크시트의 E5위치에 추가
ws.add_chart(chart, 'E5')

wb.save('openpyxl/chart_exam.xlsx')



