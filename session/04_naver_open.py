from selenium import webdriver

driver = webdriver.Chrome('/Users/사용자이름/Downloads/chromedriver')
# Selenium이 모든 자원을 가져오기까지 3초를 기다려줍니다
driver.implicitly_wait(3)
# 네이버 첫 화면을 가져와봅시다
driver.get('https://naver.com')
