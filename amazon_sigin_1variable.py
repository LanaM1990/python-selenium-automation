from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.chrome.service import Service

# driver = webdriver.Chrome(executable_path='/Users/svetlanalevinsohn/JobEasy/13-python-selenium-automation/chromedriver')
service = Service('/Users/svetlanamikolenko/Desktop/automation/python-selenium-automation/chromedriver')
driver = webdriver.Chrome(service=service)

driver.get('https://www.amazon.com/')
driver.find_element(By.ID, 'nav-orders').click()

expected_result = "Sign in"
actual_result = driver.find_element(By.XPATH, "//div[@class='a-box']//h1[@class='a-spacing-small']").text


assert expected_result == actual_result, f'Expected{expected_result} but got actual {actual_result}'
print('Test case passed')