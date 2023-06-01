# mini-python-scripts

This repository is a container for a miscellaneous assortment of single script projects done with python.
In my mind, it did not make sense to create a repo for each one of them. 
Below is a short description for each.

## array_to_clipboard

This script turns an "array" (a rectangular list of lists) into a string, which might be copied to the clipboard. 
This string is able to be pasted into a spreadsheet such as Google Sheets or Excel.
Values within a row are separated with tabs. Rows are separated with newlines. 
It does not do any kind of escaping, so it can only really handle simple numbers and strings. 

## classic_runge_kutta_4

This script uses classic RK4 (fourth order Runge-Kutta) method to approximate a solution to the given first order diffferential equation on the chosen interval.

## electron_configuration_writer

This script is used to generate both full and abbreviated electron configuration strings. 
In the simplest use case, the user inputs the number of electrons in the atom/ion of interest, and the script prints the electron configuration.

## empirical_formula_assistor

This script is used to assist in finding an empirical formula for a compound when given mass (or percent by mass) data. 
When run, the user is prompted to input each element symbol and its amount. 
After which, the script prints the mole ratio of each element to the least abundant element. The user can then input a number to scale the ratios by. 
The goal would be to find a whole number number that scales all the mole ratios to an approximate whole number.

## euler_method

This script uses Euler's method to approximate a solution to the given first order differential equation on the chosen interval.

## folder_maker

This script makes folders in the current working directory based on the names in a list of strings. It does not support nested folders though. 

## improved_euler_method

This script uses improved Euler method to approximate a solution to the given first order differential equation on the chosen interval.

## morse_translator

This script allows for translation of text to and from morse code. Note that some special characters were taken from what was used in [GBoard's morse code keyboard](https://support.google.com/accessibility/android/answer/9011881?hl=en&co=GENIE.Platform%3DAndroid).
`.` is used for "dot", `-` is used for dash, ` ` is used to separate characters, and `/` is used to separate words.
If you would like to learn morse code, I found the [Google's morse code trainer](https://morse.withgoogle.com/learn/) helpful.

## projectile_motion_w_air_resistance

This jupyter notebook was used to generate graphs describing projectile motion with air resistance present. 
These graphs also plotted the values for a projectile traveling without any air resistance as a point of comparison.
Both projectiles were simulated as launching under the same initial conditions.

## quadratic_drag

This script uses a numerical method to simulate projectile motion with quadratic drag.
It then creates a plot of range vs initial speed for a variety of launch angles.

## quick_data_calculations

This script contains some math functions that might be helpful for rudimentary data analysis. It was originally made to help me conceptualize the formulas I was needing to use by translating them into code. 

## resistance_given_power_problem_numerical_method

This script uses odd numerical techniques to solve the following physics problem. In retrospect, Newton's method would have worked much better.
"A resistor with resistance R is connected to a battery that has emf 13.0 V and internal resistance r = 0.39 Ω. For what two values of R will the power dissipated in the resistor be 80.0 W ?"

## temperature_unit_converter

This script, when run, converts the input temperature value (with a unit) into Celsius (C), Fahrenheit (F), Kelvin (K) and Rankine (R). 
