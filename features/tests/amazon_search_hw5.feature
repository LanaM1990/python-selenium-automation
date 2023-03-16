# Created by svetlanamikolenko at 2/16/23
Feature: Amazon search tests
#
#  Scenario Outline: User can search for a product on Amazon page
#    Given Open Amazon page
#    When Input text <search_word> into search field
#    When Click on search icon
#    Then Verify that text <search_result> is shown
#    Examples:
#      |search_word |search_result|
#      |coffee      | "coffee"    |
#      |mug         | "mug"       |


  Scenario Outline: User can search for a product on Amazon
    Given Open Amazon page
    When Input text <text> into search field
    When Click on search icon
    Then Verify that text <expected_result> is shown
  Examples:
     | text   | expected_result |
     | coffee | "coffee"        |
#
#  Scenario: User can see product name and product image for every search result
#    Given Open Amazon page
#    When Input text coffee into search field
#    And Click on search icon
#    Then Verify that product name is shown for every product
#    And Verify that product image is shown for every product

