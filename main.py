# pylint: disable=W0311,C0301
"""
This module contains the main function for the unit converter program.
"""

import dist
import temp
import speed
import weight

def main():
  """
  Main function for the unit converter program.
  Displays a menu of conversion options and prompts the user for input.
  Executes the corresponding conversion based on the user's choice.
  """
  while True:
    print("1. Length/Distance")
    print("2. Temperature")
    print("3. Speed")
    print("4. Weight")
    print("q. Quit")

    # get input from user
    choice = input("\nEnter your choice: ")

    if choice.lower() == "q":
      print("Goodbye!")
      break

    match (choice):
      case "1":
        result = dist.main()
      case "2":
        result = temp.main()
      case "3":
        result = speed.main()
      case "4":
        result = weight.main()
      case _:
        print("Invalid choice\n")
        continue
    if result is not None:
      print(f"{result[0]:.2f} is equal to {result[1]:.2f}\n")


if __name__ == "__main__":
  main()
