#pylint: disable=all
from setuptools import setup, find_packages

with open('requirements.txt', encoding='utf-8') as f:
  requirements = f.read().splitlines()

setup(
  name='Unit Converter',
  version='1.0',
  packages=find_packages(),
  install_requires=requirements,
  entry_points={
    'console_scripts': [
      'unit-converter = main:run',  # Replace 'main' with your actual module name and 'main_function' with your entry point
    ],
  },
  data_files=[('', ['main.py', 'ui_form.py'])],
)
