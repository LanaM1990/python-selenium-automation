# Created by svetlanamikolenko at 2/24/23
Feature: Customer service page tests


  Scenario: User can see all UI elements on the page
    Given Open Amazon page
    When Click on Customer service tab
    Then Verify that 10 UI elements on Customer page are present

