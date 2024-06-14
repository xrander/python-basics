class Employee:
    """Model employee finance."""
    def __init__(self, first, last, annual_salary):
        """Initialize employee details."""
        self.first = first.title()
        self.last = last.title()
        self.salary = annual_salary

    def give_raise(self, raise_amount=5000):
        """Add 5000 dollars to worker salary and allow for other increase"""
        self.salary += raise_amount