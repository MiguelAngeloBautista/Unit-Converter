# pylint: disable=W0311,C0301,R0903
"""
This module provides a function to convert values between different units of measurement.
"""

from pint import UnitRegistry

if __name__ != "__main__":
  from .convert import Convert
  from .console import Console
else:
  from convert import Convert # pylint: disable=E0401
  from console import Console # pylint: disable=E0401

# ==========================================GUI Version==============================================================
class Distance(Convert):
  """
  Class representing a distance converter.

  Attributes:
    units (dict): A dictionary mapping unit names to their corresponding quantities.
  """

  def __init__(self) -> None:
    super().__init__()
    self.units = {
      'Meter': self.ureg.meter,
      'Kilometer': self.ureg.kilometer,
      'Centimeter': self.ureg.centimeter,
      'Millimeter': self.ureg.millimeter,
      'Mile': self.ureg.mile,
      'Yard': self.ureg.yard,
      'Foot': self.ureg.foot,
      'Inch': self.ureg.inch
    }

# ==========================================Console Version==============================================================
def main_console() -> tuple[UnitRegistry.Quantity, UnitRegistry.Quantity]:
  ''' 
  function allows the user to convert values between different units of measurement.
  It prompts the user for the initial unit, converted unit, and the value to be converted.
  The function then performs the conversion and returns the final converted value and unit.
  
  ### Returns:
      initial_value, converted_value: A tuple containing the initial distance and the converted distance in a Pint Quantity format. e.g <Quantity(30.0, 'meter')>
  
  '''
  console = Console()
  console.units = {
    'Meter': console.ureg.meter,
    'Kilometer': console.ureg.kilometer,
    'Centimeter': console.ureg.centimeter,
    'Millimeter': console.ureg.millimeter,
    'Mile': console.ureg.mile,
    'Yard': console.ureg.yard,
    'Foot': console.ureg.foot,
    'Inch': console.ureg.inch
  }
  return console.convert()

# ==========================================Main Function==============================================================
if __name__ == "__main__":
  dist = Distance()
  result = dist.convert(1, 'Kilometer', 'Meter')
  print(result)
  result = main_console()
  print(f"{result[0]:.2f} is equal to {result[1]:.2f}\n")
  