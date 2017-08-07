from selenium import webdriver
from datetime import datetime

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')

driver = webdriver.Chrome('chromedriver', chrome_options=options)

driver.get('https://facebook.com')
driver.implicitly_wait(3)

email = driver.find_element_by_css_selector('input[type=email]')
password = driver.find_element_by_css_selector('input[type=password]')
login = driver.find_element_by_css_selector('input[type="submit"]')

email.send_keys('username@mail.com')
password.send_keys('ilovepython')
login.click()

driver.get_screenshot_as_file('{}.png'.format(datetime.now()))
driver.quit()