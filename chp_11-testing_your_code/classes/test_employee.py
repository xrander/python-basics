from employee import Employee

def test_give_default_raise():
    """Does the employee raise equate to +5000 by default"""
    employee_details = Employee("olamide", "adu", 20000)
    employee_details.give_raise()
    assert employee_details.salary == 25000

def test_other_amount_raise():
    """
    Does the employee salary increase to
    1030000 if 30000 is specified
    """
    employee_details = Employee("olamide", "adu", 1000000)
    employee_details.give_raise(30000)
    assert employee_details.salary == 1030000