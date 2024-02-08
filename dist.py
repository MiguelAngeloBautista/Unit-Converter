from pint import UnitRegistry

def main() -> tuple[UnitRegistry.Quantity, UnitRegistry.Quantity]:
  ''' 
  function allows the user to convert values between different units of measurement.
  It prompts the user for the initial unit, converted unit, and the value to be converted.
  The function then performs the conversion and returns the final converted value and unit.
  
  ### Returns:
      initial_value, converted_value: A tuple containing the initial distance and the converted distance in a Pint Quantity format. e.g <Quantity(30.0, 'meter')>
  
  '''
  # Create a Pint UnitRegistry
  ureg = UnitRegistry()

  while True:
    # Define the available units
    units = {
      'Meter': ureg.meter,
      'Kilometer': ureg.kilometer,
      'Centimeter': ureg.centimeter,
      'Millimeter': ureg.millimeter,
      'Mile': ureg.mile,
      'Yard': ureg.yard,
      'Foot': ureg.foot,
      'Inch': ureg.inch
    }

    # Prompt the user to choose the initial unit
    print("Available units:")
    for index, unit in enumerate(units.keys()):
      print(f"{index + 1}. {unit}")

    init_unit = int(input("Enter the number corresponding to the initial unit: "))
    if init_unit not in range(1, len(units) + 1):
      print("Invalid choice. Please choose a number from the list")
      continue

    # Prompt the user to choose the converted unit
    print("Available converted units:")
    for index, unit in enumerate(units.keys()):
      print(f"{index + 1}. {unit}")

    converted_unit = int(input("Enter the number corresponding to the converted unit: "))
    if converted_unit not in range(1, len(units) + 1):
      print("Invalid choice. Please choose a number from the list")
      continue

    value = input("Enter the value: ")
    try:
      value = float(value)
    except ValueError:
      print("Invalid Value. Please enter numbers only")
      continue

    # Get the initial unit based on the user's choice
    initial_unit = list(units.values())[init_unit - 1]
    initial_value = value * initial_unit

    # Get the converted unit based on the user's choice
    converted_unit = list(units.values())[converted_unit - 1]

    # Convert the value to the chosen converted unit
    converted_value = initial_value.to(converted_unit)

    return initial_value, converted_value

if __name__ == "__main__":
  main()