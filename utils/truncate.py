# pylint: disable=W0311
"""
This module provides a function to truncate a number to a specified number of decimal places.
"""
def truncate(n, decimals=0):
  """
  Truncates a number to a specified number of decimal places.

  Args:
    n (float): The number to be truncated.
    decimals (int, optional): The number of decimal places to truncate to. Defaults to 0.

  Returns:
    float: The truncated number.
  """
  multiplier = 10**decimals
  return int(n * multiplier) / multiplier
