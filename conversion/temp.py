# pylint: disable=W0311,C0301,R0903
"""
This module provides a simple unit converter for temperatures.
"""

from pint import UnitRegistry

if __name__ != "__main__":
  from .convert import Convert
  from .console import Console
else:
  from convert import Convert # pylint: disable=E0401
  from console import Console # pylint: disable=E0401

# ==========================================GUI Version==============================================================
class Temperature(Convert):
  """
  Class representing a temperature converter.

  Attributes:
    units (dict): A dictionary mapping unit names to their corresponding quantities.
  """

  def __init__(self) -> None:
    super().__init__()
    self.units = {
      'Celsius': self.ureg.degC,
      'Fahrenheit': self.ureg.degF,
      'Kelvin': self.ureg.kelvin
    }

# ==========================================Console Version==============================================================
def main_console() -> tuple[UnitRegistry.Quantity, UnitRegistry.Quantity]:
  '''
    This function allows the user to convert temperatures to their desired units
    It prompts the user for the initial temperature unit, the converted temperature unit, and the temperature value
    The function then performs the conversion and returns the final converted value and unit.

    ### Returns:
        initial_value, converted_temperature: A tuple containing the initial temperature and the converted temperature in a Pint Quantity format. e.g <Quantity(30.0, 'degC')>
  '''
  console = Console()
  console.units = {
    'Celsius': console.ureg.degC,
    'Fahrenheit': console.ureg.degF,
    'Kelvin': console.ureg.kelvin
  }
  return console.convert()

# ==========================================Main Function==============================================================
if __name__ == "__main__":
  temp = Temperature()
  result = temp.convert(26, "Celsius", "Fahrenheit")
  print(result)
  # print(f"{result[0]:.2f} is equal to {result[1]:.2f}\n")
