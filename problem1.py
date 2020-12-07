----------------------------------------------------------------------
Name:	  problem1.py
Purpose: 
Given the user input of celsius, it can convert the celsius temperature to fahrenheit 

Author: Li.B

Created:  07/12/2020
----------------------------------------------------------------------
#This gets the user input for celsius 
celsius_input = float(input("What is the temperature in celsius?: "))

#This converts celsius to fahrenheit
fahrenheit = (celsius_input * 9/5) + 32 

#This prints out the temperature in fahrenheit
print("This is your temperature in fahrenheit: " + str(fahrenheit))