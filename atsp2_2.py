from selenium import webdriver 
from selenium.webdriver.common.by import By as by
import math
driver = webdriver.Firefox()

driver.get('http://suninjuly.github.io/alert_accept.html')

driver.find_element(by.CSS_SELECTOR, '.btn').click()

driver.switch_to.alert.accept()
import time
time.sleep(2)
x = driver.find_element(by.ID, 'input_value').text

f = math.log(abs(12*math.sin(int(x))))

answer = driver.find_element(by.ID, 'answer')
answer.send_keys(str(f))

driver.find_element(by.CSS_SELECTOR, '.btn').click()

print(driver.switch_to.alert.text)
