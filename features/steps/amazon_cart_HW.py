from selenium.webdriver.common.by import By
from behave import given, when, then


@when('Click on cart')
def click_on_cart(context):
    context.driver.find_element(By.ID, 'nav-cart').click()


@then('Verify the cart is empty')
def verify_cart_is_empty(context):
    expected_result = "Your Amazon Cart is empty"
    actual_result = context.driver.find_element(By.CSS_SELECTOR, 'div.a-row.sc-your-amazon-cart-is-empty').text
    assert expected_result == actual_result, f'Expected{expected_result} but got actual{actual_result}'

