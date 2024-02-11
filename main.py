# pylint: disable=W0311,C0301,E0611,R0903,I1101
"""
This module contains the main function for the unit converter program.
"""
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow  # dont mind this error, it is a false positive. works anyway. E0611
from ui_form import Ui_MainWindow

# Import the conversion functions
import conversion
# Import Utilities
from utils.truncate import truncate

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
        result = conversion.dist.main_console()
      case "2":
        result = conversion.temp.main_console()
      case "3":
        result = conversion.speed.main_console()
      case "4":
        result = conversion.weight.main_console()
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
    self.ui.rb_dist.setChecked(True)

    # Connext radio buttons to update combobox units
    self.ui.rb_dist.toggled.connect(self.update_combobox)
    self.ui.rb_temp.toggled.connect(self.update_combobox)
    self.ui.rb_speed.toggled.connect(self.update_combobox)
    self.ui.rb_weight.toggled.connect(self.update_combobox)

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
    input_value: float = self.ui.initialValue.value()
    input_unit: str = self.ui.cb_initial.currentText()
    output_unit: str = self.ui.cb_convert.currentText()
    converted_value: float = 0.00

    if self.ui.rb_dist.isChecked():
      converted_value = conversion.dist_util.convert(input_value, input_unit, output_unit)
    elif self.ui.rb_temp.isChecked():
      converted_value = conversion.temp_util.convert(input_value, input_unit, output_unit)
    elif self.ui.rb_speed.isChecked():
      converted_value = conversion.speed_util.convert(input_value, input_unit, output_unit)
    elif self.ui.rb_weight.isChecked():
      converted_value = conversion.weight_util.convert(input_value, input_unit, output_unit)

    sanitised_value = truncate(converted_value, 6)
    self.ui.l_converted.setText(str(sanitised_value))

  def update_combobox(self):
    """
    Update the combobox based on the current tab.
    """

    if self.ui.rb_dist.isChecked():
      self.ui.cb_initial.clear()
      self.ui.cb_initial.addItems(conversion.dist_util.units.keys())
      self.ui.cb_convert.clear()
      self.ui.cb_convert.addItems(conversion.dist_util.units.keys())
    elif self.ui.rb_temp.isChecked():
      self.ui.cb_initial.clear()
      self.ui.cb_initial.addItems(conversion.temp_util.units.keys())
      self.ui.cb_convert.clear()
      self.ui.cb_convert.addItems(conversion.temp_util.units.keys())
    elif self.ui.rb_speed.isChecked():
      self.ui.cb_initial.clear()
      self.ui.cb_initial.addItems(conversion.speed_util.units.keys())
      self.ui.cb_convert.clear()
      self.ui.cb_convert.addItems(conversion.speed_util.units.keys())
    elif self.ui.rb_weight.isChecked():
      self.ui.cb_initial.clear()
      self.ui.cb_initial.addItems(conversion.weight_util.units.keys())
      self.ui.cb_convert.clear()
      self.ui.cb_convert.addItems(conversion.weight_util.units.keys())

if __name__ == "__main__":
  # main()
  app = QApplication(sys.argv)
  window = UnitConverterApp()
  window.show()
  sys.exit(app.exec())
