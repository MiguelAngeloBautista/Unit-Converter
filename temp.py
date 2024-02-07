import pint

def main():
  while True:
    # Create a Pint UnitRegistry
    ureg = pint.UnitRegistry()
    Q_ = ureg.Quantity

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

    temperature = input("Enter the temperature value: ")
    try:
        temperature = float(temperature)
    except ValueError:
      print("Invalid Value. Please enter numbers only")
      continue

    # Get the initial temperature unit based on the user's choice
    initial_unit = list(temperature_units.values())[init_temp - 1]
    initial_value = Q_(temperature, initial_unit)

    converted = []
    # Convert the temperature to other available units
    for unit_name, unit in temperature_units.items():
      if unit != initial_unit:
        converted_temperature = initial_value.to(unit)
        converted.append((converted_temperature))
        # print(f"{temperature} {initial_unit} is equal to {converted_temperature}")
    
    return converted
  


if __name__ == "__main__":
  result = main()
  print("The final value is {:.2f}".format(result[0]), "|", "{:.2f}".format(result[1]), "\n")
