from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(executable_path='/Users/svetlanamikolenko/Desktop/automation/python-selenium-automation/chromedriver')

#Amazon logo
driver.find_element(By.XPATH, "//i[@aria-label='Amazon']")
driver.find_element(By.XPATH, "//i[@class='a-icon a-icon-logo']")

#Email field
driver.find_element(By.ID, 'ap_email')
driver.find_element(By.XPATH, "//input[@name='email']")
driver.find_element(By.XPATH, "//input[@name='email' and @type='email']")

#Continue button
driver.find_element(By.ID, 'continue')
driver.find_element(By.XPATH, "//input[@aria-labelledby='continue-announce']")

#Need help button
driver.find_element(By.XPATH, "//a[contains(@data-csa-c-func-deps, 'expander-toggle')]")
driver.find_element(By.XPATH, "//a[contains(@class, 'a-link-expander')]")

#Forgot your password
driver.find_element(By.ID, 'auth-fpp-link-bottom')

#other issues with sign-in
driver.find_element(By.ID, 'ap-other-signin-issues-link')

#create your amazon account
driver.find_element(By.ID, 'createAccountSubmit')

#conditions of use
driver.find_element(By.XPATH, "//a[contains(@href, 'condition_of_use')]")
driver.find_element(By.ID, 'legalTextRow')
driver.find_element(By.XPATH, "//a[text()='Conditions of Use']")
#privacy notice
driver.find_element(By.XPATH, "//a[contains(@href, 'notification_privacy_notice')]")
driver.find_element(By.XPATH, "//div[@id='legalTextRow']/a[contains(@href, 'ap_signin_notification_privacy_notice')]")
driver.find_element(By.XPATH, "//div[@id='legalTextRow']//a[text()='Privacy Notice']"





