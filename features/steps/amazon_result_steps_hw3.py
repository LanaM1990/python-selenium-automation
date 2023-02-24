from selenium.webdriver.common.by import By
from behave import given, when, then

PRODUCT_TITLE = (By.XPATH, "//h2[@class='a-size-mini a-spacing-none a-color-base s-line-clamp-2']/a")


@when('Click on the first search result')
def click_first_search_result(context):
    search_results = context.driver.find_elements(*PRODUCT_TITLE)
    search_results[1].click()



@then('Verify that text {text} is shown')
def verify_search_result(context, text):
    expected_result = '"coffee"'
    actual_result = context.driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text
    assert expected_result == actual_result, f'Expected {expected_result} but got actual {actual_result}'






