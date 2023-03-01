from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then


PRODUCT_TITLE = (By.XPATH, "//h2[@class='a-size-mini a-spacing-none a-color-base s-line-clamp-2']/a")
PRODUCT_PRICE = (By.CSS_SELECTOR, 'span.a-price')
PRODUCT_NAME = (By.CSS_SELECTOR, "h2 span.a-size-base-plus.a-color-base.a-text-normal")
IMAGES = (By.CSS_SELECTOR, 'img[data-image-latency="s-product-image"]')

@when('Click on the first search result')
def click_first_search_result(context):
    context.driver.wait.until(EC.element_to_be_clickable(PRODUCT_PRICE))
    search_results = context.driver.find_elements(*PRODUCT_PRICE)
    search_results[1].click()



@then('Verify that text {text} is shown')
def verify_search_result(context, text):
    expected_result = '"coffee"'
    actual_result = context.driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text
    assert expected_result == actual_result, f'Expected {expected_result} but got actual {actual_result}'


@then('Verify that product name is shown for every product')
def verify_product_name(context):
    all_products = context.driver.find_elements(*PRODUCT_NAME)
    print(all_products)
    for product in all_products[:5]:
        assert product.text, f'Got no product title'


@then('Verify that product image is shown for every product')
def verify_images_present(context):
    all_images = context.driver.find_elements(*IMAGES)

    for images in all_images[:5]:
        assert images.is_displayed(), f'No image found'
    # or  assert images.get_attribute('src'), f'No image found'





