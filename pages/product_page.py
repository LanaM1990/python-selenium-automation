from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import Page

class ProductPage(Page):
    ADD_TO_CART_BUTTON = (By.ID, "add-to-cart-button")
    NEW_ARRIVALS = (By.CSS_SELECTOR, 'a.nav-a.nav-hasArrow[aria-label="New Arrivals"]')
    CATEGORY_LIST = (By.CSS_SELECTOR, 'a.mm-merch-panel ul')

    def click_add_to_cart(self):
        self.driver.find_element(*self.ADD_TO_CART_BUTTON).click()

    def hover_over_new_arrivals(self):
        new_arrivals = self.driver.find_element(*self.NEW_ARRIVALS)
        actions = ActionChains(self.driver)
        actions.move_to_element(new_arrivals)
        actions.perform()
    def verify_user_sees_deals(self):
        self.wait_for_element_appear(*self.CATEGORY_LIST)


