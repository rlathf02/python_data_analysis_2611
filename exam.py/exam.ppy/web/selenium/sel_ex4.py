
# ===========================================
# 0) 브라우저 실행 + 페이지 접속
# ===========================================
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://quotes.toscrape.com/')


# ===========================================
# 2) 다음 페이지 이동 + 반복 수집
# ===========================================

# 최대 몇 페이지까지 수집할지 제한하는 상수
# 무한 크롤링을 방지하기 위한 안전 장치
MAX_PAGES = 3

# 현재 페이지 번호를 추적하기 위한 변수
current_page = 1

results = []

while current_page <= MAX_PAGES:
    print(f'===== {current_page}페이지 수집 중 =====')

    # 새 페이지에서 다시 quote 블록 수집
    quote_blocks = driver.find_elements(By.CLASS_NAME, 'quote')

    for block in quote_blocks:
        quote_text = block.find_element(By.CLASS_NAME, 'text').text
        author = block.find_element(By.CLASS_NAME, 'author').text
        tag_elements = block.find_elements(By.CLASS_NAME, 'tag')
        tags = [t.text for t in tag_elements]

        results.append({
            'page': 1,
            'quote': quote_text,
            'author': author,
            'tags': tags
        })

    # Next 버튼 찾기
    # 'li.next a'는 class='next'를 가진 li태그 안에 있는 a태그를 의미
    # CSS_SELECTOR : CSS문법을 이용해서 HTML요소를 찾는 방법
    # Selenium에서 가장 많이 쓰이는 방식 중 하나
    next_buttons = driver.find_elements(By.CSS_SELECTOR, 'li.next a')

    if not next_buttons:
        print('다음 페이지가 없어 종료합니다.')
        break

    # 다음 페이지로 이동
    next_buttons[0].click()

    # 페이지 번호 1 증가
    current_page += 1

print('최종 수집 개수 :', len(results))

driver.quit()


