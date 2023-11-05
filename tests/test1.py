import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Tests(unittest.TestCase):
	def test1(self):
		browser = webdriver.Firefox()
		browser.get('http://suninjuly.github.io/registration1.html')
		input1 = browser.find_element(By.XPATH, "//label[text()='First name*']/following-sibling::input")
		input1.send_keys("Test")
		input2 = browser.find_element(By.XPATH, "//label[text()='Last name*']/following-sibling::input")
		input2.send_keys("Testov")
		input3 = browser.find_element(By.XPATH, "//label[text()='Email*']/following-sibling::input")
		input3.send_keys("test@mail.ru")
		time.sleep(4)
		button = browser.find_element(By.CSS_SELECTOR, "button.btn")
		button.click()
		time.sleep(4)
		welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
		welcome_text = welcome_text_elt.text
		self.assertEqual("Congratulations! You have successfully registered!", welcome_text)
	def test2(self):
		browser = webdriver.Firefox()
		browser.get('http://suninjuly.github.io/registration2.html')
		input1 = browser.find_element(By.XPATH, "//label[text()='First name*']/following-sibling::input")
		input1.send_keys("Test")
		input2 = browser.find_element(By.XPATH, "//label[text()='Last name*']/following-sibling::input")
		input2.send_keys("Testov")
		input3 = browser.find_element(By.XPATH, "//label[text()='Email*']/following-sibling::input")
		input3.send_keys("test@mail.ru")
		time.sleep(4)
		button = browser.find_element(By.CSS_SELECTOR, "button.btn")
		button.click()
		time.sleep(4)
		welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
		welcome_text = welcome_text_elt.text
		self.assertEqual("Congratulations! You have successfully registered!", welcome_text)
if __name__ == "__main__":
	unittest.main()
