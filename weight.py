# pylint: disable=W0311,C0301
from pint import UnitRegistry

def main() -> tuple[UnitRegistry.Quantity, UnitRegistry.Quantity]:
  '''
    This function allows the user to convert weights to their desired units
    It prompts the user for the initial weight unit, the converted weight unit, and the weight value
    The function then performs the conversion and returns the final converted value and unit.

    ### Returns:
        initial_value, converted_weight: A tuple containing the initial weight and the converted weight in a Pint Quantity format. e.g <Quantity(30.0, 'kilogram')>
  '''
  # Create a Pint UnitRegistry
  ureg = UnitRegistry()
  Q_ = ureg.Quantity

  while True:
    # Define the available weight units
    weight_units = {
      'Kilogram': ureg.kilogram,
      'Gram': ureg.gram,
      'Pound': ureg.pound,
      'Ounce': ureg.ounce,
      'Stone': ureg.stone,
      'Ton': ureg.ton
    }

    # Prompt the user to choose the initial weight unit
    print("Available weight units:")
    for index, unit in enumerate(weight_units.keys()):
      print(f"{index + 1}. {unit}")

    init_weight = int(input("Enter the number corresponding to the initial weight unit: "))
    if init_weight not in range(1, len(weight_units) + 1):
      print("Invalid choice. Please choose a number from the list")
      continue

    # Prompt the user to choose the converted weight unit
    print("Available converted weight units:")
    for index, unit in enumerate(weight_units.keys()):
      print(f"{index + 1}. {unit}")

    converted_weight = int(input("Enter the number corresponding to the converted weight unit: "))
    if converted_weight not in range(1, len(weight_units) + 1):
      print("Invalid choice. Please choose a number from the list")
      continue

    weight = input("Enter the weight value: ")
    try:
      weight = float(weight)
    except ValueError:
      print("Invalid Value. Please enter numbers only")
      continue

    # Get the initial weight unit based on the user's choice
    initial_unit = list(weight_units.values())[init_weight - 1]
    initial_value = Q_(weight, initial_unit)

    # Get the converted weight unit based on the user's choice
    converted_unit = list(weight_units.values())[converted_weight - 1]

    # Convert the weight to the chosen converted unit
    converted_weight = initial_value.to(converted_unit)
    
    return initial_value, converted_weight
  

if __name__ == "__main__":
  result = main()
  print("The final value is {:.2f}".format(result[0]), "|", "{:.2f}".format(result[1]), "\n")
