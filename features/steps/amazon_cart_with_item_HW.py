from selenium.webdriver.common.by import By
from behave import given, when, then



@when('Input Purses into search field')
def input_search_word(context):
    context.driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('Purses')


@when('Click on the first search result')
def click_first_search_result(context):
    search_results = context.driver.find_elements(By.XPATH, "//h2[@class='a-size-mini a-spacing-none a-color-base s-line-clamp-2']/a")
    search_results[1].click()



@when("Click on Add to Cart Button")
def click_add_to_cart(context):
    context.driver.find_element(By.ID, "add-to-cart-button").click()


@then('Verify item is in the cart')
def verify_item_in_the_cart(context):
    expected_result = "Added to Cart"
    actual_result = context.driver.find_element(By.ID, "NATC_SMART_WAGON_CONF_MSG_SUCCESS").text
    assert expected_result == actual_result, f'Expected{expected_result} but got actual{actual_result}'
    assert context.driver.find_element(By.ID, "nav-cart-count").is_displayed(), 'Cart is empty'




