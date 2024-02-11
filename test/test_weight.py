#pylint: disable=all
from unittest import TestCase
from unittest.mock import patch
import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from conversion.weight import main_console as main

class TestWeightConverter(TestCase):
    @patch('builtins.input', side_effect=['1', '2', '30'])
    def test_kg_to_gram(self, mock_input):
        initial_value, converted_weight = main()
        self.assertAlmostEqual(initial_value.magnitude, 30)
        self.assertAlmostEqual(converted_weight.magnitude, 30000, delta=.1)

    @patch('builtins.input', side_effect=['3', '4', '10'])
    def test_lb_to_ounce(self, mock_input):
        initial_value, converted_weight = main()
        self.assertAlmostEqual(initial_value.magnitude, 10)
        self.assertAlmostEqual(converted_weight.magnitude, 160, delta=.1)

    @patch('builtins.input', side_effect=['5', '6', '5'])
    def test_stone_to_ton(self, mock_input): # Ton is in US Ton not Imperial Ton
        initial_value, converted_weight = main()
        self.assertAlmostEqual(initial_value.magnitude, 5)
        self.assertAlmostEqual(converted_weight.magnitude, 0.035, delta=.1) 

    @patch('builtins.input', side_effect=['2', '1', '5000'])
    def test_gram_to_kg(self, mock_input):
        initial_value, converted_weight = main()
        self.assertAlmostEqual(initial_value.magnitude, 5000)
        self.assertAlmostEqual(converted_weight.magnitude, 5, delta=.1)

    @patch('builtins.input', side_effect=['4', '3', '100'])
    def test_ounce_to_lb(self, mock_input):
        initial_value, converted_weight = main()
        self.assertAlmostEqual(initial_value.magnitude, 100)
        self.assertAlmostEqual(converted_weight.magnitude, 6.25, delta=.1)

    @patch('builtins.input', side_effect=['6', '5', '0.5'])
    def test_ton_to_stone(self, mock_input): # Ton is in US Ton not Imperial Ton
        initial_value, converted_weight = main()
        self.assertAlmostEqual(initial_value.magnitude, 0.5)
        self.assertAlmostEqual(converted_weight.magnitude, 71.4286, delta=.1) # The immense number of decimal places doesnt matter in this case as the test is still valid. his to prevent the assertion error

if __name__ == '__main__':
    unittest.main()