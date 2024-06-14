import pytest

from employee import Employee

@pytest.fixture
def employee_details():
    """Define default employee"""
    employee_details = Employee("olamide", "adu", 1000000)
    return employee_details

def test_give_default_raise(employee_details):
    """Test if the default raise is 5000"""
    employee_details.give_raise()
    assert employee_details.salary == 1005000

def test_give_custom_raise(employee_details):
    """Test if the raise increases by 10000"""
    employee_details.give_raise(10000)
    assert employee_details.salary == 1010000

    