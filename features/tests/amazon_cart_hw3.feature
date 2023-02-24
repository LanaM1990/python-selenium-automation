# Created by svetlanamikolenko at 2/16/23
Feature: Amazon cart verification

  Scenario: User clicks on the cart and sees that its empty
   Given Open Amazon page
    When Click on cart
    Then Verify the cart is empty

  Scenario: User adds purse to the empty cart
   Given Open Amazon page
    When Input text Purses into search field
    When Click on search icon
    And  Click on the first search result
     And Click on Add to Cart Button
    Then Verify item is in the cart

