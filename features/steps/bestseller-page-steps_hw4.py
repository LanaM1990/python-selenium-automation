from selenium.webdriver.common.by import By
from behave import given, when, then

BESTSELLER_LINKS = (By.XPATH, '//div[@id="zg_header"]//div[@data-card-metrics-id="p13n-zg-nav-tab-all_zeitgeist-lists_0"]//a')

@then('Verify bestseller page has {expected_result} links in the header')
def verify_bestseller_page_links(context, expected_result):
    expected_result = int(expected_result)
    bestseller_links = context.driver.find_elements(*BESTSELLER_LINKS)
    print('\nLink count:', expected_result)
    assert len(bestseller_links) == expected_result, f'Expected{expected_result} links, but got {len(bestseller_links)}'



