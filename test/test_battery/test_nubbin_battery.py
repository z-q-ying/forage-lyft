import unittest
from datetime import date
from dateutil.relativedelta import relativedelta
from battery.nubbin_battery import NubbinBattery


class TestNubbinBattery(unittest.TestCase):
    def test_needs_service_true(self):
        cur_date = date.today()
        last_service_date = cur_date - relativedelta(years=4)
        battery = NubbinBattery(cur_date, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_needs_service_false(self):
        cur_date = date.today()
        last_service_date = cur_date - relativedelta(years=4) + relativedelta(days=1)
        battery = NubbinBattery(cur_date, last_service_date)
        self.assertFalse(battery.needs_service())
