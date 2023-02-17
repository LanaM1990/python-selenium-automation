from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(executable_path='/Users/svetlanalevinsohn/JobEasy/13-python-selenium-automation/chromedriver')

#By ID
driver.find_element(By.ID, 'twotabsearchtextbox')

#By CSS, using ID
driver.find_element(By.CSS_SELECTOR, '#twotabsearchtextbox')

#BY CSS, using class
driver.find_element(By.CSS_SELECTOR, 'span.icp-nav-flag')
#multiple classes
driver.find_element(By.CSS_SELECTOR, 'span.icp-nav-flag.icp-nav-flag-us.icp-nav-flag-lop')

#By CSS, using atributes (except ID and class)
driver.find_element(By.CSS_SELECTOR, "a[data-csa-c-content-id='nav_cs_bestsellers']")
driver.find_element(By.CSS_SELECTOR, "a[href='/gp/bestsellers/?ref_=nav_cs_bestsellers']")
#multiple attributes
driver.find_element(By.CSS_SELECTOR, "a[data-csa-c-content-id='nav_cs_bestsellers'][tabindex='0']")

#class + attribute
driver.find_element(By.CSS_SELECTOR, "a.nav-a[data-csa-c-content-id='nav_cs_bestsellers'][tabindex='0']")

#Atributtes, partial match *=
driver.find_element(By.CSS_SELECTOR, "a[href*='=nav_cs_bestsellers']")

#CSS from parent to child
driver.find_element(By.CSS_SELECTOR, '#legalTextRow a[href*=condition_of_use]')
driver.find_element(By.CSS_SELECTOR, 'div.a-section #legalTextRow a[href*=condition_of_use]')
