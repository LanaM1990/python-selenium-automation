from selenium.webdriver.common.by import By
from behave import given, when, then




@when('Click on Returns and Order')
def click_returns_and_order(context):
    context.driver.find_element(By.ID, 'nav-orders').click()


@then('Verify sign in header is shown')
def verify_signin_header(context):
    expected_result = "Sign in"
    actual_result = context.driver.find_element(By.XPATH, "//div[@class='a-box']//h1[@class='a-spacing-small']").text
    assert expected_result == actual_result, f'Expected{expected_result} but got actual {actual_result}'


@then('Verify email input field is present')
def verify_email_present(context):
    expected_result_2 = "Email or mobile phone number"
    actual_result_2 = context.driver.find_element(By.XPATH, '//label[@class="a-form-label"]').text
    assert expected_result_2 == actual_result_2, f'Expected{expected_result_2} but got actual{actual_result_2}'

