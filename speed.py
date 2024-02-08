# pylint: disable=W0311,C0301
"""
This module provides a function to convert speeds to different units.
"""

from pint import UnitRegistry

def main() -> tuple[UnitRegistry.Quantity, UnitRegistry.Quantity]:
  '''
    This function allows the user to convert speeds to their desired units
    It prompts the user for the initial speed unit, the converted speed unit, and the speed value
    The function then performs the conversion and returns the final converted value and unit.

    ### Returns:
        initial_value, converted_speed: A tuple containing the initial speed and the converted speed in a Pint Quantity format. e.g <Quantity(30.0, 'meter / second')>
  '''
  # Create a Pint UnitRegistry
  ureg = UnitRegistry()
  q_ = ureg.Quantity

  while True:
    # Define the available speed units
    speed_units = {
      'Meters per second': ureg.meter / ureg.second,
      'Kilometers per hour': ureg.kilometer / ureg.hour,
      'Miles per hour': ureg.mile / ureg.hour
    }

    # Prompt the user to choose the initial speed unit
    print("Available speed units:")
    for index, unit in enumerate(speed_units.keys()):
      print(f"{index + 1}. {unit}")

    init_speed = int(input("Enter the number corresponding to the initial speed unit: "))
    if init_speed not in range(1, len(speed_units) + 1):
      print("Invalid choice. Please choose a number from the list")
      continue

    # Prompt the user to choose the converted speed unit
    print("Available converted speed units:")
    for index, unit in enumerate(speed_units.keys()):
      print(f"{index + 1}. {unit}")

    converted_speed = int(input("Enter the number corresponding to the converted speed unit: "))
    if converted_speed not in range(1, len(speed_units) + 1):
      print("Invalid choice. Please choose a number from the list")
      continue

    speed = input("Enter the speed value: ")
    try:
      speed = float(speed)
    except ValueError:
      print("Invalid Value. Please enter numbers only")
      continue

    # Get the initial speed unit based on the user's choice
    initial_unit = list(speed_units.values())[init_speed - 1]
    initial_value = q_(speed, initial_unit)

    # Get the converted speed unit based on the user's choice
    converted_unit = list(speed_units.values())[converted_speed - 1]

    # Convert the speed to the chosen converted unit
    converted_speed = initial_value.to(converted_unit)

    return initial_value, converted_speed


if __name__ == "__main__":
  result = main()
  print(f"{result[0]:.2f} is equal to {result[1]:.2f}\n")
