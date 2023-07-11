# Created by Asi at 09/07/2023
Feature: Verify if Books are added and deleted using Library API
  # Enter feature description here
  @Library @Smoke
  Scenario: Verify AddBook API functionality
    Given the Book details which needs to be added to Library
    When we execute the AddBook PostAPI method
    Then book is successfully added
    And  status code of response should be 200

  @Library @Regression
  Scenario Outline: Verify AddBook API functionality
    Given the Book details with <isbn> and <aisle>
    When we execute the AddBook PostAPI method
    Then book is successfully added
    And status code of response should be <status_code>
      Examples:
        | isbn  | aisle | status_code |
        | fdfea | 83484 |    200      |
        | abcsd | 76422 |    200      |