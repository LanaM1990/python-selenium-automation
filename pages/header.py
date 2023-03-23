from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from pages.base_page import Page


class Header(Page):
    AMAZON_SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
    AMAZON_SEARCH_ICON = (By.ID, 'nav-search-submit-button')
    RETURN_ORDERS_ICON = (By.ID, 'nav-orders')
    CART_ICON = (By.ID, 'nav-cart')
    LANG_OPTIONS = (By.ID, 'icp-nav-flyout')
    SPANISH_LANG = (By.CSS_SELECTOR, 'a.nav-link.nav-item')
    DEPARTMENT_SELECTION = (By.ID, 'searchDropdownBox')


    def input_search_text(self, text):
        self.input_text(text, *self.AMAZON_SEARCH_FIELD)

    def click_search(self):
        self.click(*self.AMAZON_SEARCH_ICON)

    def click_returns_orders(self):
        self.click(*self.RETURN_ORDERS_ICON)

    def click_cart(self):
        self.wait_for_element_click(*self.CART_ICON)

    def hover_lang_options(self):
        lang_options = self.find_element(*self.LANG_OPTIONS)
        actions = ActionChains(self.driver)
        actions.move_to_element(lang_options)
        actions.perform()

    def verify_lang_shown(self):
        self.wait_for_element_appear(*self.SPANISH_LANG)

    def select_dept_by_alias(self, alias):
        department_dd = self.find_element(*self.DEPARTMENT_SELECTION)
        select = Select(department_dd)
        select.select_by_value(f'search-alias={alias}')




