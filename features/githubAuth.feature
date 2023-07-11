# Created by Asi at 09/07/2023
Feature: GitHub API Authentication validation
  # Enter feature description here

  @Smoke
  Scenario: Session management check with invalid password
    Given I have github auth credentials with invalid password
    When I hit getRepo API of github
    Then status code of response should be 401