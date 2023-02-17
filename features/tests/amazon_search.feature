# Created by svetlanamikolenko at 2/16/23
Feature: Amazon search tests


  Scenario: User can search for a product on Amazon
    Given Open Amazon page
    When Input text coffee
    When Click on search icon
    Then Verify that text "coffee" is shown