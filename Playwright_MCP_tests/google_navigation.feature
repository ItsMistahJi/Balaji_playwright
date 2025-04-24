Feature: Google Navigation

  Scenario: Validate Google homepage title
    Given I navigate to "https://google.com"
    When I capture the title of the page
    Then the title should be "Google"
    And I take a screenshot of the current page