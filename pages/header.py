from selenium.webdriver.common.by import By
from pages.base_page import Page


class Header(Page):
    AMAZON_SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
    AMAZON_SEARCH_ICON = (By.ID, 'nav-search-submit-button')
    RETURN_ORDERS_ICON = (By.ID, 'nav-orders')
    CART_ICON = (By.ID, 'nav-cart')

    def input_search_text(self, text):
        self.input_text(text, *self.AMAZON_SEARCH_FIELD)

    def click_search(self):
        self.click(*self.AMAZON_SEARCH_ICON)

    def click_returns_orders(self):
        self.click(*self.RETURN_ORDERS_ICON)

    def click_cart(self):
        self.wait_for_element_click(*self.CART_ICON)
