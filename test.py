import unittest
from tempreture import celsius_to_farenheit, celsius_to_kelvin


class TestTempConversion(unittest.TestCase):

    def test_celsius_to_fahrentheit(self):
        self.assertEqual(celsius_to_farenheit(21), 69.8)

    def test_celsius_to_fahrentheit_float(self):
        self.assertEqual(celsius_to_farenheit(21.2), 70.16)

if __name__ == '__main__':
    unittest.main()