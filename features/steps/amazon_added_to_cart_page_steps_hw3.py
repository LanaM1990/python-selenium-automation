from selenium.webdriver.common.by import By
from behave import given, when, then


CART_EMPTY = (By.CSS_SELECTOR, 'div.a-row.sc-your-amazon-cart-is-empty')


@then('Verify the cart is empty')
def verify_cart_is_empty(context):
    expected_result = "Your Amazon Cart is empty"
    actual_result = context.driver.find_element(*CART_EMPTY).text
    assert expected_result == actual_result, f'Expected{expected_result} but got actual{actual_result}'


@then('Verify item is in the cart')
def verify_item_in_the_cart(context):
    expected_result = "Added to Cart"
    actual_result = context.driver.find_element(By.ID, "NATC_SMART_WAGON_CONF_MSG_SUCCESS").text
    assert expected_result == actual_result, f'Expected{expected_result} but got actual{actual_result}'
    assert context.driver.find_element(By.ID, "nav-cart-count").is_displayed(), 'Cart is empty'


