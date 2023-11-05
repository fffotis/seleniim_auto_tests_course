import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"

@pytest.fixture(scope='class')
def driver():
	print('\nstart browser')
	driver = webdriver.Firefox()
	yield driver
	print('\nquit browser')
	driver.quit()

class TestMainPage():
	def test1(self, driver):
		print("\nstart test1")
		driver.get(link)
		driver.find_element(By.CSS_SELECTOR, "#login_link")
		print("\nfinish test1")
	def test2(self, driver):
		print("\nstart test2")
		driver.get(link)
		driver.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")
		print("\nfinish test2")
