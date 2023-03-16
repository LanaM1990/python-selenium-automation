from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Page

class SignInPage(Page):
    def verify_signin(self):
        self.wait.until(EC.url_contains('https://www.amazon.com/ap/signin'))

