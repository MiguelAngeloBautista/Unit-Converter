#pylint: disable=all
from unittest import TestCase
from unittest.mock import patch
import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dist import main_console as main

class TestDistanceConverter(TestCase):
    @patch('builtins.input', side_effect=['1', '2', '100'])
    def test_meter_to_kilometer(self, mock_input):
        initial_value, converted_distance = main()
        self.assertAlmostEqual(initial_value.magnitude, 100)
        self.assertAlmostEqual(converted_distance.magnitude, 0.1)

    @patch('builtins.input', side_effect=['2', '1', '0.1'])
    def test_kilometer_to_meter(self, mock_input):
        initial_value, converted_distance = main()
        self.assertAlmostEqual(initial_value.magnitude, 0.1)
        self.assertAlmostEqual(converted_distance.magnitude, 100)

    @patch('builtins.input', side_effect=['1', '3', '100'])
    def test_meter_to_centimeter(self, mock_input):
        initial_value, converted_distance = main()
        self.assertAlmostEqual(initial_value.magnitude, 100)
        self.assertAlmostEqual(converted_distance.magnitude, 10000)

    @patch('builtins.input', side_effect=['3', '2', '10000'])
    def test_centimeter_to_kilometer(self, mock_input):
        initial_value, converted_distance = main()
        self.assertAlmostEqual(initial_value.magnitude, 10000)
        self.assertAlmostEqual(converted_distance.magnitude, 0.1)

    @patch('builtins.input', side_effect=['2', '3', '0.1'])
    def test_kilometer_to_centimeter(self, mock_input):
        initial_value, converted_distance = main()
        self.assertAlmostEqual(initial_value.magnitude, 0.1)
        self.assertAlmostEqual(converted_distance.magnitude, 10000)

    @patch('builtins.input', side_effect=['3', '1', '10000'])
    def test_centimeter_to_meter(self, mock_input):
        initial_value, converted_distance = main()
        self.assertAlmostEqual(initial_value.magnitude, 10000)
        self.assertAlmostEqual(converted_distance.magnitude, 100)

if __name__ == '__main__':
    unittest.main()