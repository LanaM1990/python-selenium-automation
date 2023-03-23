from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


HAM_MENU = (By.ID, "nav-hamburger-menu")
FOOTER_LINKS = (By.CSS_SELECTOR, 'table.navFooterMoreOnAmazon td.navFooterDescItem')
BESTSELLERS_TAB = (By.CSS_SELECTOR, 'a[data-csa-c-content-id="nav_cs_bestsellers"]')
CUSTOMER_SERVICE_TAB = (By.CSS_SELECTOR, 'a.nav-a[data-csa-c-slot-id="nav_cs_3"]')
SIGN_IN_BUTTON = (By.CSS_SELECTOR, '#nav-signin-tooltip a.nav-action-button')



@given('Open Amazon page')
def open_amazon(context):
    context.app.main_page.open_main()
    # context.driver.get('https://www.amazon.com/')


@when('Click on Customer service tab')
def click_customer_ser_tab(context):
    context.driver.find_element(*CUSTOMER_SERVICE_TAB).click()


@when('Input text {text} into search field')
def input_search_word(context, text):
    context.app.header.input_search_text(text)
    # context.driver.find_element(*AMAZON_SEARCH_FIELD).send_keys(text)


@when('Click on search icon')
def click_search_button(context):
    context.app.header.click_search()
    # context.driver.find_element(*AMAZON_SEARCH_ICON).click()

@when('Click on cart')
def click_on_cart(context):
    context.app.header.click_cart()
    # context.driver.wait.until(EC.element_to_be_clickable(CART_ICON)).click()
    # context.driver.find_element(*CART_ICON).click()


@when('Click on Returns and Order')
def click_returns_and_order(context):
    context.app.header.click_returns_orders()
    # context.driver.find_element(By.ID, 'nav-orders').click()


@when('Click on Bestsellers tab')
def click_bestsellers_tab(context):
    context.driver.find_element(*BESTSELLERS_TAB).click()


@when('Click Sign In from popup')
def click_singin_popup(context):
    context.driver.wait.until(EC.element_to_be_clickable(SIGN_IN_BUTTON)).click()

@when('Wait for {sec} sec')
def wait_for_sec(context, sec):
    sleep(int(sec))


@when('Hover over language options')
def hover_lang_options(context):
    context.app.header.hover_lang_options()


@when('Click on hum menu')
def click_hum_menu(context):
    context.hum_menu = context.driver.find_element(*HAM_MENU)
    context.hum_menu.click()


@when('Select department by alias {alias}')
def select_dept_by_alias(context, alias):
    context.app.header.select_dept_by_alias(alias)


@then('Verify Sign in popup shown')
def click_singin_popup_shown(context):
    context.driver.wait.until(
        EC.element_to_be_clickable(SIGN_IN_BUTTON),
        message='Sign in popup is not clickable')


@then('Verify Sign in popup disappears')
def click_singin_popup_disappers(context):
    context.driver.wait.until(
        EC.invisibility_of_element_located(SIGN_IN_BUTTON),
        message='Signin btn did not disappear')


@then('Verify hamburger menu icon present')
def verify_ham_menu_present(context):
    # print('\n Find elements:')
    context.hum_menu = context.driver.find_element(*HAM_MENU)
    context.driver.refresh()
    # print(elements)
    # assert len(elements) == 1, f'Expected 1 element but got {len(elements)}'


@then('Verify that footer has {expected_amount} links')
def verify_footer_link_count(context, expected_amount):
    expected_amount = int(expected_amount)
    footer_links = context.driver.find_elements(*FOOTER_LINKS)
    # print(footer_links)
    # print('\nLink count:', len(footer_links))
    assert len(footer_links) == expected_amount, f'Expected {expected_amount} links, but got {len(footer_links)}'

@then('Verify Spanish option present')
def verify_lang_shown(context):
    sleep(4)
    context.app.header.verify_lang_shown()

