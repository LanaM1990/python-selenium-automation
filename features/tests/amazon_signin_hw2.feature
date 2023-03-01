# Created by svetlanamikolenko at 2/16/23
Feature: Amazon sign in page verification


  Scenario: Logged out user sees sign in page when clicking on Returns and Orders
    Given Open Amazon page
    When Click on Returns and Order
    Then Verify sign in header is shown
    And Verify email input field is present

  Scenario: Sign in page can be opened from sign In popup
    Given Open Amazon page
    When Click Sign In from popup
    Then Verify Sign in page opens



