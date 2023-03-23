# Created by svetlanamikolenko at 3/6/23
Feature: Terms and conditions tests


  Scenario:  User can open and close Amazon Privacy Notice
    Given Open Amazon T&C page
    When Store original windows
    And Click on Amazon Privacy Notice link
    And Switch to the newly opened window
    Then Verify Amazon Privacy Notice page is opened
    And User can close new window
    And Switch back to original
