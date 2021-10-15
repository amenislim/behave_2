Feature: slideanelement
@critical
  Scenario: slide the bar
    Given :the user navigate in ur
    When the user slide the bar until he get a percentage
    Then he sees a percentage under the bar