from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

CART = (By.ID, 'nav-cart-count')
GO_TO_CART = (By.XPATH, '//span[@id="sw-gtc"]//a')
PRODUCT_NAME = (By.CSS_SELECTOR, 'span.a-list-item a[class="a-link-normal sc-product-link"]')


# @when('Open cart page')
# def open_cart_page(context):
#     sleep(4)
#     context.driver.find_element(*GO_TO_CART).click()

@when('Open cart page')
def open_cart_page(context):
    sleep(4)
    context.driver.get('https://www.amazon.com/gp/cart/view.html?ref_=sw_gtc')


@then('Verify cart has {expected_count} item(s)')
def verify_cart_count(context, expected_count):
    actual_text = context.driver.find_element(*CART).text
    assert expected_count == actual_text, f'Expected {expected_count} item(s) but got {actual_text}'

@then('Verify cart has correct product')
def cart_has_correct_product(context):
    actual_name = context.driver.find_element(*PRODUCT_NAME).text
    assert context.product_name[:30] in actual_name, f'Expected {context.product_name} but got {actual_name}'
