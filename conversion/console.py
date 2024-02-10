# pylint: disable=W0311,C0301,R0903
'''
  This module provides an abtract class for performing unit conversions in console version.
'''

import abc
from pint import UnitRegistry

class Console(abc.ABC):
  """
  A class for performing unit conversions in the console.

  Attributes:
    ureg (UnitRegistry): The unit registry for performing conversions.
    q_ (function): A function for creating quantities.
    units (dict): A dictionary mapping unit names to their corresponding quantities.

  Methods:
    convert: Convert a value from one unit to another.
  """

  def __init__(self) -> None:
    self.ureg = UnitRegistry()
    self.q_ = self.ureg.Quantity
    self.units = {}

  def convert(self) -> tuple[UnitRegistry.Quantity, UnitRegistry.Quantity]:
    """
    Convert the given value from the input unit to the desired unit.

    Returns:
      tuple[UnitRegistry.Quantity, UnitRegistry.Quantity]: A tuple containing the converted value in the desired unit and the original value in the input unit.
    """
    while True:
      # Prompt the user to choose the initial weight unit
      print("Available weight units:")
      for index, unit in enumerate(self.units.keys()):
        print(f"{index + 1}. {unit}")

      init_weight = int(input("Enter the number corresponding to the initial weight unit: "))
      if init_weight not in range(1, len(self.units) + 1):
        print("Invalid choice. Please choose a number from the list")
        continue

      # Prompt the user to choose the converted weight unit
      print("Available converted weight units:")
      for index, unit in enumerate(self.units.keys()):
        print(f"{index + 1}. {unit}")

      converted_weight = int(input("Enter the number corresponding to the converted weight unit: "))
      if converted_weight not in range(1, len(self.units) + 1):
        print("Invalid choice. Please choose a number from the list")
        continue

      value = input("Enter the weight value: ")
      try:
        value = float(value)
      except ValueError:
        print("Invalid Value. Please enter numbers only")
        continue

      # Get the initial weight unit based on the user's choice
      initial_unit = list(self.units.values())[init_weight - 1]
      initial_value = self.q_(value, initial_unit)

      # Get the converted weight unit based on the user's choice
      converted_unit = list(self.units.values())[converted_weight - 1]

      # Convert the weight to the chosen converted unit
      converted_value = initial_value.to(converted_unit)
      return initial_value, converted_value
