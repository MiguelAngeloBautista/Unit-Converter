#pylint: disable=all
from unittest import TestCase
from unittest.mock import patch
import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from conversion.speed import main

class TestSpeedConverter(TestCase):
    @patch('builtins.input', side_effect=['1', '2', '30'])
    def test_mps_to_kmph(self, mock_input):
        initial_value, converted_speed = main()
        self.assertAlmostEqual(initial_value.magnitude, 30)
        self.assertAlmostEqual(converted_speed.magnitude, 108, delta=.1)

    @patch('builtins.input', side_effect=['2', '1', '100'])
    def test_kmph_to_mps(self, mock_input):
        initial_value, converted_speed = main()
        self.assertAlmostEqual(initial_value.magnitude, 100)
        self.assertAlmostEqual(converted_speed.magnitude, 27.7778, delta=.1)

    @patch('builtins.input', side_effect=['1', '3', '60'])
    def test_mps_to_mph(self, mock_input):
        initial_value, converted_speed = main()
        self.assertAlmostEqual(initial_value.magnitude, 60)
        self.assertAlmostEqual(converted_speed.magnitude, 134.236, delta=.1)

    @patch('builtins.input', side_effect=['3', '2', '80'])
    def test_mph_to_kmph(self, mock_input):
        initial_value, converted_speed = main()
        self.assertAlmostEqual(initial_value.magnitude, 80)
        self.assertAlmostEqual(converted_speed.magnitude, 128.747, delta=.1)

    @patch('builtins.input', side_effect=['2', '3', '50'])
    def test_kmph_to_mph(self, mock_input):
        initial_value, converted_speed = main()
        self.assertAlmostEqual(initial_value.magnitude, 50)
        self.assertAlmostEqual(converted_speed.magnitude, 31.0686, delta=.1)

    @patch('builtins.input', side_effect=['3', '1', '70'])
    def test_mph_to_mps(self, mock_input):
        initial_value, converted_speed = main()
        self.assertAlmostEqual(initial_value.magnitude, 70)
        self.assertAlmostEqual(converted_speed.magnitude, 31.2928, delta=.1)

if __name__ == '__main__':
    unittest.main()