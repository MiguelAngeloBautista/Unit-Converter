# pylint: disable=W0311,C0301,R0903
"""
This module provides a function to convert speeds to different units.
"""

from pint import UnitRegistry

if __name__ != "__main__":
  from .convert import Convert
  from .console import Console
else:
  from convert import Convert # pylint: disable=E0401
  from console import Console # pylint: disable=E0401

# ==========================================GUI Version==============================================================
class Speed(Convert):
  """
  Class representing a speed converter.

  Attributes:
    units (dict): A dictionary mapping unit names to their corresponding quantities.
  """

  def __init__(self) -> None:
    super().__init__()
    self.units = {
      'Meters per second': self.ureg.meter / self.ureg.second,
      'Kilometers per hour': self.ureg.kilometer / self.ureg.hour,
      'Miles per hour': self.ureg.mile / self.ureg.hour
    }

# ==========================================Console Version==============================================================
def main_console() -> tuple[UnitRegistry.Quantity, UnitRegistry.Quantity]:
  '''
    This function allows the user to convert speeds to their desired units
    It prompts the user for the initial speed unit, the converted speed unit, and the speed value
    The function then performs the conversion and returns the final converted value and unit.

    ### Returns:
        initial_value, converted_speed: A tuple containing the initial speed and the converted speed in a Pint Quantity format. e.g <Quantity(30.0, 'meter / second')>
  '''
  console = Console()
  console.units = {
    'Meters per second': console.ureg.meter / console.ureg.second,
    'Kilometers per hour': console.ureg.kilometer / console.ureg.hour,
    'Miles per hour': console.ureg.mile / console.ureg.hour
  }
  return console.convert()

# ==========================================Main Function==============================================================
if __name__ == "__main__":
  speed = Speed()
  result = speed.convert(60, "Kilometers per hour", "Miles per hour")
  print(result)
  # print(f"{result[0]:.2f} is equal to {result[1]:.2f}\n")
