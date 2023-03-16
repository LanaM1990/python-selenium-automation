from pages.main_page import MainPage
from pages.header import Header
from pages.search_results_page import SearchResultPage
from pages.sign_in_page import SignInPage
from pages.added_to_cart_page import Cart
from pages.product_page import ProductPage
class Application:

    def __init__(self, driver):
        self.driver = driver
        self.main_page = MainPage(self.driver)
        self.header = Header(self.driver)
        self.search_results_page = SearchResultPage(self.driver)
        self.sign_in_page = SignInPage(self.driver)
        self.added_to_cart_page = Cart(self.driver)
        self.product_page = ProductPage(self.driver)


