# Created by svetlanamikolenko at 2/26/23
Feature:  Tests for product page


#  Scenario:  User can select colors
#    Given Open Amazon product B08JHKQPBV page
#    Then Verify user can click through colors


  Scenario:  User can select colors
    Given Open Amazon product B07BJKRR25 page
    Then Verify user can click through colors

  Scenario: User can see deals
    Given Open Amazon product B074TBCSC8 page
    When Hover over New Arrivals
    Then Verify user can see deals
