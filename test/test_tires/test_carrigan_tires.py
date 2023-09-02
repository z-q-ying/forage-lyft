import unittest
from tires.carrigan_tires import CarriganTires


class TestCarriganTires(unittest.TestCase):
    def test_needs_service_true(self):
        tire = CarriganTires([0.5, 0.4, 0.9, 0.8])
        self.assertTrue(tire.needs_service())

    def test_needs_service_false(self):
        tire = CarriganTires([0.5, 0.4, 0.7, 0.8])
        self.assertFalse(tire.needs_service())
