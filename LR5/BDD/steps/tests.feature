Feature: Testing the FieldCollector
  Scenario: Try collect 2 fields
    Given a goods list
    """
    [{"title": "Ковер", "price": 2000, "color": "green"},{"title": "Диван для отдыха", "price": 5300, "color": "black"}]
    """
    And fields #1 title and #2 color
    When we call function with that data we get result
    Then we can assert this data with the tuple
    """
    [{"title": "Ковер", "color": "green"},{"title": "Диван для отдыха", "color": "black"}]
    """
  Scenario: Try collect 1 field
    Given a goods list
    """
    [{"title": "Ковер", "price": 2000, "color": "green"},{"title": "Диван для отдыха", "price": 5300, "color": "black"}]
    """
    And fields #1 title
    When we call function with that data we get result
    Then we can assert this data with the tuple
    """
    ["Ковер", "Диван для отдыха"]
    """