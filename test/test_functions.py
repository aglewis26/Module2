"""
Author: Adam Lewis
Program: camper_age_input.py
Date:9/8/2020

Program that accepts an integer for years and returns a converted integer for months.
"""
import unittest
from main import camper_age_input

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(72, camper_age_input.conver_to_months(6))


if __name__ == '__main__':
    unittest.main()
