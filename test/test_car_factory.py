# This Python script contains unit tests for two car models: Calliope and Palindrome

import unittest
from datetime import date
from car_factory import CarFactory
from dateutil.relativedelta import relativedelta


class TestCarFactory(unittest.TestCase):

    def test_calliope_a(self):
        cur_mileage = 30001
        last_service_mileage = 0
        cur_date = date.today()
        last_service_date = cur_date - relativedelta(years=3)
        calliope = CarFactory.create_calliope(cur_date, last_service_date, cur_mileage, last_service_mileage)
        self.assertTrue(calliope.needs_service())

    def test_calliope_b(self):
        cur_mileage = 30001
        last_service_mileage = 0
        cur_date = date.today()
        last_service_date = cur_date - relativedelta(years=2)
        calliope = CarFactory.create_calliope(cur_date, last_service_date, cur_mileage, last_service_mileage)
        self.assertTrue(calliope.needs_service())

    def test_calliope_c(self):
        cur_mileage = 50001
        last_service_mileage = 30000
        cur_date = date.today()
        last_service_date = cur_date - relativedelta(years=3)
        calliope = CarFactory.create_calliope(cur_date, last_service_date,  cur_mileage, last_service_mileage)
        self.assertTrue(calliope.needs_service())

    def test_calliope_d(self):
        cur_mileage = 50001
        last_service_mileage = 30000
        cur_date = date.today()
        last_service_date = cur_date - relativedelta(years=1)
        calliope = CarFactory.create_calliope(cur_date, last_service_date, cur_mileage,  last_service_mileage)
        self.assertFalse(calliope.needs_service())

    def test_palindrome_a(self):
        cur_date = date.today()
        last_service_date = cur_date - relativedelta(years=3)
        warning_light_is_on = True
        palindrome = CarFactory.create_palindrome(cur_date, last_service_date, warning_light_is_on)
        self.assertTrue(palindrome.needs_service())

    def test_palindrome_b(self):
        cur_date = date.today()
        last_service_date = cur_date - relativedelta(years=1)
        warning_light_is_on = True
        palindrome = CarFactory.create_palindrome(cur_date, last_service_date, warning_light_is_on)
        self.assertTrue(palindrome.needs_service())

    def test_palindrome_c(self):
        cur_date = date.today()
        last_service_date = cur_date - relativedelta(years=3)
        warning_light_is_on = False
        palindrome = CarFactory.create_palindrome(cur_date, last_service_date, warning_light_is_on)
        self.assertTrue(palindrome.needs_service())

    def test_palindrome_d(self):
        cur_date = date.today()
        last_service_date = cur_date - relativedelta(years=1)
        warning_light_is_on = False
        palindrome = CarFactory.create_palindrome(cur_date, last_service_date, warning_light_is_on)
        self.assertFalse(palindrome.needs_service())
