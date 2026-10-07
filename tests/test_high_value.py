from lib.high_value import *


"""
Check if value_first and value_second is an integer
"""
def test_check_value_first_return_int():
    values = HighValue(8, 4)
    is_first_value_int = isinstance(values.value_first, int)
    assert is_first_value_int == True


def test_check_value_second_return_int():
    values = HighValue(8, 4)
    is_second_value_int = isinstance(values.value_second, int)
    assert is_second_value_int == True

"""
Check "First value is higher" returns when value_first 
is greater than value_second
"""

def test_check_first_value_returns_first_value_when_greater_than_second_value():
    values = HighValue(8, 4)
    result = values.get_highest()
    assert result == "First value is higher"

"""
Check "Second value is higher" returns when value_first 
is less than value_second
"""

def test_check_second_value_return_second_value_when_greater_than_first_value():
    values = HighValue(3, 9)
    result = values.get_highest()
    assert result == "Second value is higher"

"""
Check "Values are equal" returns when value_first 
and value_second are the same
"""

def test_check_values_are_equal_returns_when_values_are_equal():
    values = HighValue(4, 4)
    result = values.get_highest()
    assert result == "Values are equal"

"""
Check value_first has increased when the selection
for add is "first"
"""

def test_value_first_increases_when_selection_first():
    values = HighValue(2, 3)
    values.add(3, "first")
    assert values.value_first == 5 

"""
Check value_second has increased when the selection
for add is "second"
"""
def test_value_second_increases_when_selection_second():
    values = HighValue(2, 3)
    values.add(3, "second")
    assert values.value_second == 6


"""
Check value_first has decreased when the selection
for add is "first" and the number is negative
"""
def test_value_first_decreases_when_selection_first_and_negative():
    values = HighValue(2, 3)
    values.add(-3, "first")
    assert values.value_first == -1


"""
Check value_second has decreased when the selection
for add is "second" and the number is negative
"""
def test_value_second_decreases_when_selection_second_and_negative():
    values = HighValue(2, 3)
    values.add(-3, "second")
    assert values.value_second == 0
