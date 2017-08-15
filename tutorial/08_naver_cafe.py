# 08_naver.cafe.py
from selenium import webdriver
import time

driver = webdriver.Chrome('/Users/beomi/Downloads/chromedriver')
driver.implicitly_wait(3)
driver.get('https://nid.naver.com/nidlogin.login')

input_id = driver.find_element_by_css_selector('#id')
input_pw = driver.find_element_by_css_selector('#pw')
login_button = driver.find_element_by_css_selector(
    '#frmNIDLogin > fieldset > input[type="submit"]'
    )

input_id.send_keys('')
input_pw.send_keys('')
login_button.click()

# url = 'http://cafe.naver.com/joonggonara?iframe_url=/ArticleList.nhn%3Fsearch.clubid=10050146%26search.menuid=334%26search.boardtype=L'

# driver.get(url)
# time.sleep(3)
# driver.switch_to_frame('cafe_main')
# selector = '#main-area > div:nth-child(8) > form > table > tbody > tr > td.board-list > span > span > a'
# contents = driver.find_elements_by_css_selector(selector)

# for post in contents:
#     print(post.text)

# driver.quit()
