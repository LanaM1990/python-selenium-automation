from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

CART_ICON = (By.ID, 'nav-cart')
ADD_TO_CART_BUTTON = (By.ID, "add-to-cart-button")
PRODUCT_NAME = (By.ID, "productTitle")
COLOR_OPTIONS = (By.CSS_SELECTOR, '#variation_color_name li')
CURRENT_COLOR = (By.CSS_SELECTOR, '#variation_color_name .selection')

@given('Open Amazon product {product_id} page')
def open_product(context, product_id):
    context.driver.get(f'https://www.amazon.com/gp/product/{product_id}/')



@when('Click on cart')
def click_on_cart(context):
    context.driver.wait.until(EC.element_to_be_clickable(CART_ICON)).click()
    # context.driver.find_element(*CART_ICON).click()


@when("Click on Add to Cart Button")
def click_add_to_cart(context):
    context.driver.find_element(*ADD_TO_CART_BUTTON).click()


@when('Store product name')
def get_product_name(context):
    context.product_name = context.driver.find_element(*PRODUCT_NAME).text
    # print(f'Current product:{context.product_name}')

@then('Verify user can click through colors')
def verify_click_thr_colors(context):
    all_color_options = context.driver.find_elements(*COLOR_OPTIONS)
    print('All colors:', all_color_options)
    expected_colors = ['Black', 'Blue, Over Dye', 'Bright White', 'Dark Blue Vintage', 'Dark Indigo/Rinsed']
    actual_colors = []

    for color in all_color_options[:5]:
        color.click()
        current_color = context.driver.find_element(*CURRENT_COLOR).text
        print('Current color: ', current_color)

        actual_colors += [current_color]
    assert expected_colors == actual_colors, f'Expected {expected_colors} but got {actual_colors}'
