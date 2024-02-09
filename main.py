# pylint: disable=W0311,C0301,E0611,R0903
"""
This module contains the main function for the unit converter program.
"""
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow  # dont mind this error, it is a false positive. works anyway. E0611
from ui_form import Ui_MainWindow


import dist
import temp
import speed
import weight

def console():
  """
  Console function for the unit converter program in console.
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
        result = dist.main_console()
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


class UnitConverterApp(QMainWindow):
  """
  The main application window for the unit converter program.
  """

  def __init__(self):
    super().__init__()

    # Set up the UI from the generated code
    self.ui = Ui_MainWindow()
    self.ui.setupUi(self)

    # Connect the button click to the conversion function
    self.ui.pushButton.clicked.connect(self.convert_units)

  def convert_units(self):
    """
    Convert units based on user input.

    This method retrieves the input values and units, performs the conversion,
    and updates the output.

    Returns:
      None
    """
    # Add your unit conversion logic here
    input_value = self.ui.initialValue.value()
    input_unit = self.ui.cb_initial.currentText()
    output_unit = self.ui.cb_convert.currentText()

    # Perform the conversion and update the output spin box
    converted_value = dist.main(input_value, input_unit, output_unit)

    self.ui.convertedValue.setValue(converted_value)

if __name__ == "__main__":
  # main()
  app = QApplication(sys.argv)
  window = UnitConverterApp()
  window.show()
  sys.exit(app.exec())
