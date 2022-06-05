# mini-python-scripts

This repository is a container for a miscellaneous assortment of single script projects done with python.
In my mind, it did not make sense to create a repo for each one of them. 
Below is a short description for each.

## array_to_clipboard

This script turns an "array" (a rectangular list of lists) into a string, which might be copied to the clipboard. 
This string is able to be pasted into a spreadsheet such as Google Sheets or Excel.
Values within a row are separated with tabs. Rows are separated with newlines. 
It does not do any kind of escaping, so it can only really handle simple numbers and strings. 

## electron_configuration_writer

This script is used to generate both full and abbreviated electron configuration strings. 
In the simplest use case, the user inputs the number of electrons in the atom/ion of interest, and the script prints the electorn configuration.

## empirical_formula_assistor

This script is used to assist in finding an empirical formula for a compound when given mass (or percent by mass) data. 
When run, the user is prompted to input each element symbol and its amount. 
After which, the script prints the mole ratio of each element to the least abundant element. The user can then input a number to scale the ratios by. 
The goal would be to find a whole number number that scales all the mole ratios to an approximate whole number.

## folder_maker

This script makes folders in the current working directory based on the names in a list of strings. It does not support nested folders though. 

## quick_data_calculations

This script contains some math functions that might be helpful for rudimentary data analysis. It was originally made to help me conceptualize the formulas I was needing to use by translating them into code. 

## temperature_unit_converter

This script, when run, converts the input temperure value (with a unit) into Celcius (C), Fahrenheit (F), Kelvin (K) and Rankine (R). 
