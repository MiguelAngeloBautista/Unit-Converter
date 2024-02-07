from pint import UnitRegistry
from typing import List, Union
ureg = UnitRegistry()


INPUT_PROMPT = "Enter your choice: "
INVALID_CHOICE_MSG = "Invalid Units. Please choose from the above list\n"

metric_units = {"km": ureg.kilometers, "m": ureg.meters, "cm": ureg.centimeters, "mm": ureg.millimeters, "um": ureg.micrometers, "nm": ureg.nanometers}
imperial_units = {"mi": ureg.miles, "yd": ureg.yards, "ft": ureg.feet, "in": ureg.inches}

units = {**metric_units, **imperial_units}

def main() -> list[Union[float, str]]:
  """
  This function allows the user to convert values between different units of measurement.
  It prompts the user for the initial unit, converted unit, and the value to be converted.
  The function then performs the conversion and returns the final converted value and unit.
  
  ### Returns:
      [final_value.magnitude, final_value.units]: The final converted value(float) and unit(str) as a list
  
  """

  while True:
    # Show the user the available units
    print([x for x in metric_units.keys()])
    print([x for x in imperial_units.keys()])
    print("q. Back")

    # get input from user
    initial_unit = input("\nEnter Initial Unit: ")
    if initial_unit.lower() == "q":
      break
    final_unit = input("Enter Converted Unit: ")
    if final_unit.lower() == "q":
      break

    if initial_unit not in units.keys() or final_unit not in units.keys():
      print(INVALID_CHOICE_MSG)
      continue

    initial_value = input("Enter Value: ")
    try:
      initial_value = float(initial_value)
    except ValueError:
      print("Invalid Value. Please enter numbers only")
      continue

    # Convert value int Pint quantity
    initial_value = initial_value * units[initial_unit]

    final_value = initial_value.to(units[final_unit])
    return [final_value.magnitude, final_value.units]

if __name__ == "__main__":
  main()