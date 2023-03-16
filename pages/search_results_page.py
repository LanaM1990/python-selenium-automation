from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Page


class SearchResultPage(Page):
    SEARCH_RESULT = (By.XPATH, "//span[@class='a-color-state a-text-bold']")
    PRODUCT_PRICE = (By.CSS_SELECTOR, 'span.a-price')
    def verify_search_result(self, expected_text):
        self.verify_text(expected_text, *self.SEARCH_RESULT)

    def click_first_result(self):
        self.wait.until(EC.element_to_be_clickable(self.PRODUCT_PRICE))
        search_results = self.driver.find_elements(*self.PRODUCT_PRICE)
        search_results[1].click()


