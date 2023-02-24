from selenium.webdriver.common.by import By
from behave import given, when, then

ADD_TO_CART_BUTTON = (By.ID, "add-to-cart-button")

@when("Click on Add to Cart Button")
def click_add_to_cart(context):
    context.driver.find_element(*ADD_TO_CART_BUTTON).click()


