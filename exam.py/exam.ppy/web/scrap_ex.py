
# requests 모듈 => 웹페이지를 요청하고 응답 데이터를 받을 수 있음
import requests as req
from bs4 import BeautifulSoup 


response = req.get ('http://naver.com/')
print(response)

'''
대표적인 HTTP 상태 코드
- 200 : 요청 성공
- 301, 302: 다른 URL로 이동
- 403 : 접근 거부
- 404: 요청한 페이지 없음
-500: 서버 내부 오류
'''

html_doc = """<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

#print(html_doc)
soup = BeautifulSoup (html_doc,'html.parser')
#soup을 이용해서 html_doc문자열 파싱, 그 내용을 soup 변수에 대입

a_list = soup.select('a')
print('=== a태그들 리스트 ===')
print(a_list)

print('=== a태그 리스트 중 첫번째 ===')
print(a_list[0])

print('=== a태그 리스트 중 첫번째 텍스트===')
print(a_list[0].text)

print('=== a태그 리스트 중 첫번째 링크===')
print(a_list[0],[href])

print('=== a태그 리스트에 있는 텍스트 모두 출력===')
for a in a_list:
    print(a.text)

print('=== a태그 리스트에 있는 링크 모두 출력===')
for link in a_list:
    print(link['href'])
    

