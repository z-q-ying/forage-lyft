import unittest
from tires.octoprime_tires import OctoprimeTires

class TestOctoprimeTires(unittest.TestCase):
    def test_needs_service_true(self):
        tire = OctoprimeTires([0.8, 0.8, 0.9, 0.8])
        self.assertTrue(tire.needs_service())

    def test_needs_service_false(self):
        tire = OctoprimeTires([0.5, 0.4, 0.9, 0.8])
        self.assertFalse(tire.needs_service())