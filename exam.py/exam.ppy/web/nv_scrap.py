
import requests as req
from bs4 import BeautifulSoup

request_headers = {
    'User-Agent': (
        'Mozilla/5.0 (Windows NT 10.0;Win64; x64) '
        'AppleWebKit/537.36 (KHTML, like Gecko) '
        'Chrome/71.0.3578.98 Safari/537.36'
    )
}

response = req.get('https://news.naver.com', request_headers)
# print(response)
# print(response.text)

soup = BeautifulSoup(response.text, 'html.parser')

content = soup.select('.cnf_news_item')
print(content[0].text)

print('== class로 선택, 반복문으로 텍스트 출력')
for c in content:
    print(c.text)
    

