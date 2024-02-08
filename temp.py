from pint import UnitRegistry

def main() -> tuple[UnitRegistry.Quantity, UnitRegistry.Quantity]:
  '''
    This function allows the user to convert temperatures to their desired units
    It prompts the user for the initial temperature unit, the converted temperature unit, and the temperature value
    The function then performs the conversion and returns the final converted value and unit.

    ### Returns:
        initial_value, converted_temperature: A tuple containing the initial temperature and the converted temperature in a Pint Quantity format. e.g <Quantity(30.0, 'degC')>
  '''
  # Create a Pint UnitRegistry
  ureg = UnitRegistry()
  Q_ = ureg.Quantity

  while True:
# Define the available temperature units
    temperature_units = {
      'Celsius': ureg.degC,
      'Fahrenheit': ureg.degF,
      'Kelvin': ureg.kelvin
    }

    # Prompt the user to choose the initial temperature unit
    print("Available temperature units:")
    for index, unit in enumerate(temperature_units.keys()):
      print(f"{index + 1}. {unit}")

    init_temp = int(input("Enter the number corresponding to the initial temperature unit: "))
    if init_temp not in range(1, len(temperature_units) + 1):
      print("Invalid choice. Please choose a number from the list")
      continue

    conv_temp = int(input("Enter the number corresponding to the converted temperature unit: "))
    if conv_temp not in range(1, len(temperature_units) + 1):
      print("Invalid choice. Please choose a number from the list")
      continue

    temperature = input("Enter the temperature value: ")
    try:
        temperature = float(temperature)
    except ValueError:
      print("Invalid Value. Please enter numbers only")
      continue

    # Get the initial temperature unit based on the user's choice
    initial_unit = list(temperature_units.values())[init_temp - 1]
    converted_unit = list(temperature_units.values())[conv_temp - 1]

    initial_value = Q_(temperature, initial_unit)
    converted_temperature = initial_value.to(converted_unit)

    return initial_value, converted_temperature
  


if __name__ == "__main__":
  result = main()
  print("The final value is {:.2f}".format(result[0]), "|", "{:.2f}".format(result[1]), "\n")
