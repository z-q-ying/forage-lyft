import unittest
from engine.capulet_engine import CapuletEngine


class TestCapuletEngine(unittest.TestCase):
    def test_needs_service_true(self):
        cur_mileage = 30001
        last_service_mileage = 0
        engine = CapuletEngine(cur_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_needs_service_false(self):
        cur_mileage = 50000
        last_service_mileage = 20010
        engine = CapuletEngine(cur_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())
