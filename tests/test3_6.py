import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def test(url):
	driver = webdriver.Firefox()
	driver.get(url)
	time.sleep(10)
	button = driver.find_element(By.CLASS_NAME, 'navbar__auth_login') 
	button.click()
	driver.find_element(By.ID, 'id_login_email').send_keys('fortressing06@gmail.com')
	driver.find_element(By.ID, 'id_login_password').send_keys('Fotis06ing...')
	driver.find_element(By.CLASS_NAME, 'sign-form__btn').click()
	time.sleep(10)
	text = driver.find_element(By.CSS_SELECTOR, '.string-quiz__textarea')
	text.click()
	answer = math.log(int(time.time()))
	text.send_keys(str(answer))
	button = driver.find_element(By.CLASS_NAME, 'submit-submission')
	button.click()
	time.sleep(5)
	t = driver.find_element(By.CLASS_NAME, 'smart-hints__hint').text
	if t != 'Correct!':
		print(t)

x = '''
https://stepik.org/lesson/236895/step/1
https://stepik.org/lesson/236896/step/1
https://stepik.org/lesson/236897/step/1
https://stepik.org/lesson/236898/step/1
https://stepik.org/lesson/236899/step/1
https://stepik.org/lesson/236903/step/1
https://stepik.org/lesson/236904/step/1
https://stepik.org/lesson/236905/step/1'''.split()

for i in x:
	test(i)