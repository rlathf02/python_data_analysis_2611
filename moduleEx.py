
'''
#직접 생성한 모듈 불러오기
import ex1
#선택적으로 불러오기
from ex1 import funcA, funcB
print(ex1
'''
'''
# 수학 모듈
# 수학 계산 기능을 제공하는 모듈
# 제곱근, 삼각함수, 원주율 등을 포함
import math
#16의 제곱근 계산 
print(math.sqrt(16))
# 2의 3제곱
print(math.pow(2,3))
'''


'''
# 난수 모듈
# 무작위 값을 생성하는 모듈
# 게임, 추천, 테스트 데이터에 사용
import random
#1부터 100까지 랜덤으로 숫자 한개 추출
print(random.randint(1,100))
'''
#날짜/시간 모듈
#날짜와 시간을 다루는 모듈
#현재 시간 확인, 날짜 계산 사용
'''
import datetime
#현재 시간 확인, 날짜 계산 사용
print(datetime.datetime())


#시간 제어 모듈
#시간 흐름을 제어하는 모듈
#프로그램이 잠시 멈출 때 사용

import time

#프로그램을 3초 동안 멈춤
time.sleep(3)
#3초가 지난 후 출력
print("3초 후 실행")
'''

#시스템 모듈
#파이썬 실행 환경을 다루는 모듈
'''
import sys
#현재 사용중인 파이썬 버전 출력
print(sys.version)
'''

#운영체제 모듈
#운영체제(os)와 관련된 기능 제공
#파일/폴더 경로 처리에 사용
'''
import os

# 현재 작업중인 폴더 경로 출력
print(os.getcwd())

'''

#데이터 형식 모듈
#json형식으로 데이터를 변환
# - json : 데이터를 약속된 모양으로 적는 방식("key":"value")
# 웹, API 저장에 사용
# -API : 프로그램끼리 대화하는 방법(규칙)
'''
import json
data = {
    'name':'jin',
    'age' : 22
}
print(json.dumps(data))
'''

# 정규표현식 모듈
# 문자열 패턴 검사 모듈
# 형식 확인(아이디,이메일)에 사용
'''
import re
#문자열이 hi로 시작하는지 확인
print(bool(re.match('hi, ''hi python')))
'''

# csv 파일 모듈
# csv(엑셀) 파일을 읽고 쓰는 모듈
# 데이터 저장/분석 기초에 사용
'''
import csv
#csv 파일에 한 줄 데이터를 저장
with open('test.csv','w',newline='') as f:
    csv.writer(f).writerow(['name','score'])
'''

# 자료구조 모듈
# 자료구조를 편하게 쓰도록 도와줌
# 카운트,큐,딕셔너리 확장 기능 제공

from collections import Counter
#문자열에서 각 글자의 개수를 셈
print(Counter('apple'))
































































































