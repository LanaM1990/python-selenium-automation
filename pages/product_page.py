from selenium.webdriver.common.by import By
from pages.base_page import Page

class ProductPage(Page):
    ADD_TO_CART_BUTTON = (By.ID, "add-to-cart-button")

    def click_add_to_cart(self):
        self.driver.find_element(*self.ADD_TO_CART_BUTTON).click()