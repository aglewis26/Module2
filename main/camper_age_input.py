"""
Author: Adam Lewis
Program: camper_age_input.py
Date:9/8/2020

Program that accepts an integer for years and returns a converted integer for months.
"""
import constants
from main import constants


def convert_to_months(years):
    months = years * constants.MONTHS
    return months


if __name__ == '__main__':
    age_in_years = input("Enter your childs age:")
    age_in_months = convert_to_months(int(age_in_years))
    print("{} years is {} months".format(age_in_years, age_in_months))
