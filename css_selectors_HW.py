from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(executable_path='/Users/svetlanalevinsohn/JobEasy/13-python-selenium-automation/chromedriver')

#Amazon_logo by Class
driver.find_element(By.CSS_SELECTOR, 'i.a-icon.a-icon-logo')

#Create account by Attribute
driver.find_element(By.CSS_SELECTOR, 'h1[class="a-spacing-small"]')

#"Name" Field by ID
driver.find_element(By.CSS_SELECTOR, '#ap_customer_name')

#"Mobile number and email" field by ID
driver.find_element(By.CSS_SELECTOR, '#ap_email')

#"password" field by ID
driver.find_element(By.CSS_SELECTOR, '#ap_password')
#"Password" field by Multiple classes
driver.find_element(By.CSS_SELECTOR, 'input.a-input-text.auth-required-field.auth-require-password-validation')

#"Re-enter Password" field by ID
driver.find_element(By.CSS_SELECTOR, '#ap_password_check')

# Under Re-enter password text by Class
driver.find_element(By.CSS_SELECTOR, 'div.a-box.a-alert-inline.auth-inlined-information-message')

#"Continue" button by Class
driver.find_element(By.CSS_SELECTOR, 'input.a-button-input')

#"Conditions of use" by attributes (partial match *=)
driver.find_element(By.CSS_SELECTOR, 'a[href*="register_notification_condition_of_use"]')

#"Privacy notice" by attributes
driver.find_element(By.CSS_SELECTOR, 'a[href*="register_notification_privacy_notice"]')

#"Sign in" button by Class
driver.find_element(By.CSS_SELECTOR, 'a.a-link-emphasis')


