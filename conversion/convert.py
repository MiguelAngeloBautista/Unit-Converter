# pylint: disable=W0311,C0301,R0903
'''
  This module provides an abtract class for performing unit conversions.
'''

import abc

from pint import UnitRegistry

class Convert(abc.ABC):
  """
  A class for performing unit conversions.

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

  def convert(self, i_value: int, i_unit: str, c_unit: str) -> tuple[UnitRegistry.Quantity, UnitRegistry.Quantity]:
    """
    Convert the given value from the input unit to the desired unit.

    Args:
      i_value (int): The value to be converted.
      i_unit (str): The input unit of measurement.
      c_unit (str): The desired unit of measurement.

    Returns:
      tuple[UnitRegistry.Quantity, UnitRegistry.Quantity]: A tuple containing the converted value in the desired unit and the original value in the input unit.
    """
    try:
      value = float(i_value)
    except ValueError:
      print("Invalid Value. Please enter numbers only")

    # Get the initial weight unit based on the user's choice
    initial_unit = self.units[i_unit]
    initial_value = self.q_(value, initial_unit)

    # Get the converted weight unit based on the user's choice
    converted_unit = self.units[c_unit]

    # Convert the weight to the chosen converted unit
    converted_value = initial_value.to(converted_unit)

    return converted_value.magnitude
