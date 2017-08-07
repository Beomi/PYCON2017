from selenium import webdriver

driver = webdriver.Chrome('chromedriver')
driver.implicitly_wait(3)
driver.get('https://naver.com')

input_id = driver.find_element_by_css_selector('#id')
input_pw = driver.find_element_by_css_selector('#pw')
login_button = driver.find_element_by_css_selector('#frmNIDLogin > fieldset > span > input[type="submit"]')

input_id.send_keys('userid')
input_pw.send_keys('userpassword')
login_button.click()


driver.get('https://order.pay.naver.com/home?tabMenu=POINT_TOTAL')
point_list = driver.find_elements_by_css_selector('div.info_space > p')

for point in point_list:
    print(point.text)

driver.quit()
