from selenium.webdriver.common.by import By
from behave import given, when, then


@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when('Input text coffee')
def input_search_word(context):
    context.driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('coffee')


@when('Click on search icon')
def click_search_button(context):
    context.driver.find_element(By.ID, 'nav-search-submit-button').click()


@then('Verify that text "coffee" is shown')
def verify_search_result(context):
    expected_result = '"coffee"'
    actual_result = context.driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text
    assert expected_result == actual_result, f'Expected {expected_result} but got actual {actual_result}'
