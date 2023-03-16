from selenium.webdriver.common.by import By
from pages.base_page import Page

class Cart(Page):
    CART_EMPTY = (By.CSS_SELECTOR, 'div.a-row.sc-your-amazon-cart-is-empty')
    ADDED_TO_CART_TEXT = (By.ID, "NATC_SMART_WAGON_CONF_MSG_SUCCESS")
    CART_ITEM_COUNT = (By.ID, "nav-cart-count")

    def verify_cart_empty_text(self, expected_cart_text):
        expected_result = expected_cart_text
        actual_result = self.driver.find_element(*self.CART_EMPTY).text
        assert expected_result == actual_result, f'Expected{expected_result} but got actual{actual_result}'


    def verify_cart_empty(self):
        expected_result = "Your Amazon Cart is empty"
        actual_result = self.driver.find_element(*self.CART_EMPTY).text
        assert expected_result == actual_result, f'Expected{expected_result} but got actual{actual_result}'


    def verify_item_in_cart(self):
        expected_result = "Added to Cart"
        actual_result = self.driver.find_element(*self.ADDED_TO_CART_TEXT).text
        assert expected_result == actual_result, f'Expected{expected_result} but got actual{actual_result}'
        assert self.driver.find_element(*self.CART_ITEM_COUNT).is_displayed(), 'Cart is empty'


