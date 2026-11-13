# 브라우저를 실행하고 조작하는 객체
from selenium import webdriver

# 요소를 찾을 때 사용하는 선택 방식 지정도구
from selenium.webdriver.common.by import By

# 1) 브라우저 실행
driver = webdriver.Chrome()
# driver = webdriver.Firefox()

# 2) 웹페이지 접속
driver.get('https://quotes.toscrape.com/')

# 3) 요소 하나 찾기
quote = driver.find_element(By.CLASS_NAME, 'text')
print(quote.text)

# 3-1) 요소 여러 개 찾기
quotes = driver.find_elements(By.CLASS_NAME, 'text')
for quote in quotes:
    print(quote.text)

# 브라우저 종료
driver.quit()

