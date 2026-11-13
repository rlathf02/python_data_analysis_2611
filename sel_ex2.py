"""
연습 사이트: https://quotes.toscrape.com
"""

from selenium import webdriver
from selenium.webdriver.common.by import By


# -------------------------------------------------
# 공통: 드라이버 실행 및 1페이지 접속
# -------------------------------------------------
driver = webdriver.Chrome()
driver.get("https://quotes.toscrape.com")


# =================================================
# 문제 1 (기초)
# =================================================
"""
[문제 1]
1페이지에서 모든 명언(text)과 저자(author)를 출력하세요.

출력 형식:
명언 - 저자

조건:
- find_elements()를 사용하세요.
- 각 quote 블록 안에서 다시 요소를 찾으세요.
"""
print("\n===== 정답 1 - 1페이지 : 명언 + 저자 출력 =====")
quote_blocks = driver.find_elements(By.CLASS_NAME, 'quote')

for block in quote_blocks:
    quote_text = block.find_element(By.CLASS_NAME, 'text').text
    author = block.find_element(By.CLASS_NAME, 'author').text
    print(quote_text, '-', author)


# =================================================
# 문제 2 (중급)
# =================================================
"""
[문제 2]
1페이지에서 각 명언의 태그 개수를 함께 출력하세요.

출력 형식 예:
명언 - 저자 (태그 3개)

조건:
- 태그는 class="tag" 입니다.
- 태그는 여러 개일 수 있습니다.
- len()을 활용하세요.
"""
print("\n===== 정답 2 - 1페이지 : 태그 개수까지 출력 =====")
quote_blocks = driver.find_elements(By.CLASS_NAME, 'quote')

for block in quote_blocks:
    quote_text = block.find_element(By.CLASS_NAME, 'text').text
    author = block.find_element(By.CLASS_NAME, 'author').text
    tag_elements = block.find_elements(By.CLASS_NAME, 'tag')
    print(f"{quote_text} - {author} (태그 : {len(tag_elements)})")


# =================================================
# 문제 3 (중상)
# =================================================
"""
[문제 3]
2페이지까지 이동하여 총 몇 개의 명언을 수집했는지 출력하세요.

조건:
- Next 버튼을 클릭하세요.
- 반복문을 사용하세요.
- 페이지 이동 후 다시 요소를 수집하세요.
"""
print("\n===== 정답 3 - 2페이지까지 수집 후 총 개수 출력 =====")
total_quotes = 0
current_page = 1
MAX_PAGES = 2

while current_page <= MAX_PAGES:
    quote_blocks = driver.find_elements(By.CLASS_NAME,'quote')
    total_quotes += len(quote_blocks)
    
    # 2페이지까지니까, 1페이지에서만 Next를 누르면 됨
    if current_page < MAX_PAGES:
        next_buttons = driver.find_elements(By.CSS_SELECTOR, 'li.next a')
        if not next_buttons:
            break
        next_buttons[0].click()

    current_page += 1

print("2페이지까지 총 명언 개수 :", total_quotes)


# =================================================
# 문제 4 (활용)
# =================================================
"""
[문제 4]
3페이지까지 수집하면서, 태그에 "love"가 포함된 명언만 출력하세요.

출력 형식:
[LOVE] 명언 - 저자

조건:
- 태그 목록(tags) 안에 "love"가 있으면 출력합니다.
"""
print("\n===== 정답 4 - 3페이지까지 : love 태그가 있는 명언만 출력 =====")
driver.get('https://quotes.toscrape.com')

current_page = 1
MAX_PAGES = 3

while current_page <= MAX_PAGES:
    quote_blocks = driver.find_elements(By.CLASS_NAME, 'quote')

    for block in quote_blocks:
        quote_text = block.find_element(By.CLASS_NAME, 'text').text
        author = block.find_element(By.CLASS_NAME, 'author').text
        tag_elements = block.find_elements(By.CLASS_NAME, 'tag')
        tags = [t.text for t in tag_elements]

        if 'love' in tags:
            print(f"[LOVE] {quote_text} - {author}")

    if current_page < MAX_PAGES:
        next_buttons = driver.find_elements(By.CSS_SELECTOR, 'li.next a')
        if not next_buttons:
            break
        next_buttons[0].click()

    current_page += 1


# =================================================
# 문제 5 (도전)
# =================================================
"""
[문제 5]
3페이지까지 수집한 뒤, 저자별로 명언이 몇 개 있는지 출력하세요.

출력 예:
Albert Einstein : 2개
Mark Twain : 3개

조건:
- 딕셔너리를 사용하세요.
- key = author, value = 개수
"""
print("\n===== 정답5 - 3페이지까지 : 저자별 명언 개수 집계 =====")
driver.get('https://quotes.toscrape.com')

author_count = {}
current_page = 1
MAX_PAGES = 3

while current_page <= MAX_PAGES:
    quote_blocks = driver.find_elements(By.CLASS_NAME, 'quote')

    for block in quote_blocks:
        author = block.find_element(By.CLASS_NAME, 'author').text

        # 딕셔너리 집계 패턴
        # author가 없으면 0에서 시작해서 1씩 증가
        author_count[author] = author_count.get(author, 0) + 1

    if current_page < MAX_PAGES:
        next_buttons = driver.find_elements(By.CSS_SELECTOR, 'li.next a')
        if not next_buttons:
            break
        next_buttons[0].click()

    current_page += 1

for author, count in author_count.items():
    print(f"{author} : {count}개")


