from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

BESTSELLER_LINKS = (By.CSS_SELECTOR, '#zg_header a')
FIRST_LINK = (By.CSS_SELECTOR, 'a[href*=Best-Sellers]')
TEXT = (By.CSS_SELECTOR, 'span#zg_banner_text')

@then('Verify bestseller page has {expected_result} links in the header')
def verify_bestseller_page_links(context, expected_result):
    expected_result = int(expected_result)
    context.bestseller_links = context.driver.find_elements(*BESTSELLER_LINKS)
    # print('\nLink count:', expected_result)
    assert len(context.bestseller_links) == expected_result, f'Expected{expected_result} links, but got {len(context.bestseller_links)}'


@then('Click on each top link and verify correct page opens')
def click_each_link_and_verify(context):

    expected_titles = ['Best Sellers', 'New Releases', 'Movers & Shakers', 'Most Wished For', 'Gift Ideas']

    for i in range(len(expected_titles)):
        link = context.driver.find_elements(*BESTSELLER_LINKS)[i]
        link.click()

        header_text = context.driver.find_element(*TEXT).text
        assert expected_titles[i] in header_text, f'Expected{expected_titles} in {header_text}, but got no such text'


@then('Verify that correct page opens')
def verify_correct_page_opens(context):
    context.bestseller_links = context.driver.find_element(*BESTSELLER_LINKS).text
    header_text = context.driver.find_element(*TEXT).text
    assert context.bestseller_links in header_text, f'Expected{context.bestseller_links} in {header_text}'
