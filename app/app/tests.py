"""
Sample tests
"""
from django.test import SimpleTestCase

from app import calc

class CalcTests(SimpleTestCase):
    """Test the calc module"""

    def test_add_numbers(self): ## The methid name must start with the prefix: test_
        """Test adding numbers together"""
        res = calc.add(5,6)

        self.assertEqual(res,11)

    def test_subtract_numbers(self):
        res = calc.subtract(10,15)

        self.assertEqual(res,5)


## either group all the tests in 1 directory and this dir must conatin a __init__.py
## or place tests.py module inside each app