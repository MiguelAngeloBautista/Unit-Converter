#pylint: disable=all
from unittest import TestCase
from unittest.mock import patch
import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from conversion.temp import main_console as main

class TestTemperatureConverter(TestCase):
    @patch('builtins.input', side_effect=['1', '2', '100'])
    def test_celsius_to_fahrenheit(self, mock_input):
        initial_value, converted_temperature = main()
        self.assertAlmostEqual(initial_value.magnitude, 100)
        self.assertAlmostEqual(converted_temperature.magnitude, 212)

    @patch('builtins.input', side_effect=['2', '1', '212'])
    def test_fahrenheit_to_celsius(self, mock_input):
        initial_value, converted_temperature = main()
        self.assertAlmostEqual(initial_value.magnitude, 212)
        self.assertAlmostEqual(converted_temperature.magnitude, 100)

    @patch('builtins.input', side_effect=['1', '3', '100'])
    def test_celsius_to_kelvin(self, mock_input):
        initial_value, converted_temperature = main()
        self.assertAlmostEqual(initial_value.magnitude, 100)
        self.assertAlmostEqual(converted_temperature.magnitude, 373.15)

    @patch('builtins.input', side_effect=['3', '2', '373.15'])
    def test_kelvin_to_fahrenheit(self, mock_input):
        initial_value, converted_temperature = main()
        self.assertAlmostEqual(initial_value.magnitude, 373.15)
        self.assertAlmostEqual(converted_temperature.magnitude, 212)

    @patch('builtins.input', side_effect=['2', '3', '212'])
    def test_fahrenheit_to_kelvin(self, mock_input):
        initial_value, converted_temperature = main()
        self.assertAlmostEqual(initial_value.magnitude, 212)
        self.assertAlmostEqual(converted_temperature.magnitude, 373.15)

    @patch('builtins.input', side_effect=['3', '1', '373.15'])
    def test_kelvin_to_celsius(self, mock_input):
        initial_value, converted_temperature = main()
        self.assertAlmostEqual(initial_value.magnitude, 373.15)
        self.assertAlmostEqual(converted_temperature.magnitude, 100)

if __name__ == '__main__':
    unittest.main()