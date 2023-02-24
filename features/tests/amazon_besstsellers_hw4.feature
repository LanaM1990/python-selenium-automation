# Created by svetlanamikolenko at 2/22/23
Feature: Amazon bestsellers page


  Scenario: User can open Bestsellers page and see all the links
    Given Open Amazon page
    When Click on Bestsellers tab
    Then Verify bestseller page has 5 links in the header

