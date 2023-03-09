# Created by svetlanamikolenko at 3/6/23
Feature: Tests for 404 page


  Scenario: User is able to navigate to Amazon
    Given  Open Amazon product 887NBHJFHFHJDN page
    And Store original window
    When Click on a dog image
    And Switch to new window
    Then Verify blog is opened
    And Close blog
    And Return to original window