# Created by svetlanamikolenko at 2/22/23
Feature: Amazon main page tests


  Scenario: User can see hamburger menu
    Given Open Amazon page
    Then Verify hamburger menu icon present

  Scenario: Footer has correct amount of links
    Given Open Amazon page
    Then Verify that footer has 42 links

