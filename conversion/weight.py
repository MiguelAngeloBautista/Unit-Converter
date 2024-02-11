# pylint: disable=W0311,C0301,R0903
'''
This module provides a function for converting weights to different units.
'''

from pint import UnitRegistry

if __name__ != "__main__":
  from .convert import Convert
  from .console import Console
else:
  from convert import Convert # pylint: disable=E0401
  from console import Console # pylint: disable=E0401

# ==========================================GUI Version==============================================================
class Weight(Convert):
  """
  Class representing a weight converter.

  Attributes:
    units (dict): A dictionary mapping unit names to their corresponding quantities.
  """

  def __init__(self) -> None:
    super().__init__()
    self.units = {
      'Kilogram': self.ureg.kilogram,
      'Gram': self.ureg.gram,
      'Pound': self.ureg.pound,
      'Ounce': self.ureg.ounce,
      'Stone': self.ureg.stone,
      'Ton': self.ureg.ton
    }

# ==========================================Console Version==============================================================
def main_console() -> tuple[UnitRegistry.Quantity, UnitRegistry.Quantity]:
  '''
  This function allows the user to convert weights to their desired units.
  It prompts the user for the initial weight unit, the converted weight unit, and the weight value.
  The function then performs the conversion and returns the final converted value and unit.

  ### Returns:
      initial_value, converted_weight: A tuple containing the initial weight and the converted weight in a Pint Quantity format. e.g <Quantity(30.0, 'kilogram')>
  '''
  console = Console()
  console.units = {
    'Kilogram': console.ureg.kilogram,
    'Gram': console.ureg.gram,
    'Pound': console.ureg.pound,
    'Ounce': console.ureg.ounce,
    'Stone': console.ureg.stone,
    'Ton': console.ureg.ton
  }

  return console.convert()

# ==========================================Main Function==============================================================
if __name__ == "__main__":
  weight = Weight()
  result = weight.convert(80, "Kilogram", "Pound")
  print(result)
  result = main_console()
  print(f"{result[0]:.2f} is equal to {result[1]:.2f}\n")
