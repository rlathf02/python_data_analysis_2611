from openpyxl import *
from openpyxl.styles import PatternFill

#셀 배경 색 바꾸기 
wb = Workbook()
ws = wb.active

#헤더
ws['A1'] = '이름'
ws['B1'] = '국어'
ws['C1'] = '수학'

color = PatternFill(fill_type='solid', fgColor='FFFF00')

# 반복문을 통해 셀의 배경색 바꾸기
for cell in ws[1]: # 1행 전체
    cell.fill = color

wb.save('openpyxl/bg_color.xlsx')

# 색상 코드
# 빨강 : FF0000
# 노랑 : FFFF00
# 초록 : 00FF00
# 파랑 : 0000FF
# 회색 : D9D9D9