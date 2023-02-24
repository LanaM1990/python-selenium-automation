from selenium.webdriver.common.by import By
from behave import given, when, then

AMAZON_SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
AMAZON_SEARCH_ICON = (By.ID, 'nav-search-submit-button')
HAM_MENU = (By.ID, "nav-hamburger-menu")
FOOTER_LINKS = (By.CSS_SELECTOR, 'table.navFooterMoreOnAmazon td.navFooterDescItem')
BESTSELLERS_TAB = (By.CSS_SELECTOR, 'a[data-csa-c-content-id="nav_cs_bestsellers"]')
CUSTOMER_SERVICE_TAB = (By.CSS_SELECTOR, 'a.nav-a[data-csa-c-slot-id="nav_cs_3"]')



@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when('Click on Customer service tab')
def click_customer_ser_tab(context):
    context.driver.find_element(*CUSTOMER_SERVICE_TAB).click()


@when('Input text {text} into search field')
def input_search_word(context, text):
    context.driver.find_element(*AMAZON_SEARCH_FIELD).send_keys(text)


@when('Click on search icon')
def click_search_button(context):
    context.driver.find_element(*AMAZON_SEARCH_ICON).click()


@when('Click on Bestsellers tab')
def click_bestsellers_tab(context):
    context.driver.find_element(*BESTSELLERS_TAB).click()



@then('Verify hamburger menu icon present')
def verify_ham_menu_present(context):
    print('\n Find elements:')
    elements = context.driver.find_elements(*HAM_MENU)
    print(elements)
    assert len(elements) == 1, f'Expected 1 element but got {len(elements)}'


@then('Verify that footer has {expected_amount} links')
def verify_footer_link_count(context, expected_amount):
    expected_amount = int(expected_amount)
    footer_links = context.driver.find_elements(*FOOTER_LINKS)
    # print(footer_links)
    print('\nLink count:', len(footer_links))
    assert len(footer_links) == expected_amount, f'Expected {expected_amount} links, but got {len(footer_links)}'
