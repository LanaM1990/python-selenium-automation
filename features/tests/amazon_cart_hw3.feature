# Created by svetlanamikolenko at 2/16/23
Feature: Amazon empty cart verification

  Scenario: User clicks on the cart and sees that its empty
   Given Open Amazon page
    When Click on cart
    Then Verify the cart is empty

 Scenario Outline: User clicks on the cart and sees that its empty
   Given Open Amazon page
    When Click on cart
    Then Verify <expected_cart_text> text present
  Examples:
  | expected_cart_text       |
  | Your Amazon Cart is empty|

  Scenario: User adds purse to the empty cart
   Given Open Amazon page
    When Input text Purses into search field
    When Click on search icon
    And  Click on the first search result
     And Click on Add to Cart Button
    Then Verify item is in the cart

   Scenario: User can add a product to the cart
    Given Open Amazon page
    When Input text Tritan farm to Table Pitcher into search field
    When Click on search icon
    And Click on the first search result
    And Store product name
    And Click on Add to Cart Button
    And Open cart page
    Then Verify cart has 1 item(s)
    And Verify cart has correct product



