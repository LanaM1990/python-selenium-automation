from selenium.webdriver.common.by import By
from behave import given, when, then

CUSTOMER_PAGE_UI_ELEMENTS = (By.CSS_SELECTOR, 'div.issue-card-container div.issue-card-wrapper')


@then('Verify that {expected_amount} UI elements on Customer page are present')
def verify_ui_elements_on_customer_serv_page(context, expected_amount):
    expected_amount = int(expected_amount)
    customer_service_elements = context.driver.find_elements(*CUSTOMER_PAGE_UI_ELEMENTS)
    assert len(customer_service_elements) == expected_amount, f'Expected {expected_amount} elements, but got {len(customer_service_elements)}'

