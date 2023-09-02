import unittest
from engine.willoughby_engine import WilloughbyEngine


class TestWilloughbyEngine(unittest.TestCase):
    def test_needs_service_true(self):
        cur_mileage = 70000
        last_service_mileage = 9999
        engine = WilloughbyEngine(cur_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_needs_service_false(self):
        cur_mileage = 70000
        last_service_mileage = 10000
        engine = WilloughbyEngine(cur_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())
