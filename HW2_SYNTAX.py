#This program asks the user for their age.The program then outputs how many decades the user has been alive and the square root of their age.

import math

#input
variable = int(input("What is your age?"))

#Calculations
decades = (variable) / 10
root = math.sqrt(variable)

#Print_Statements
print ("You  have lived", decades, "decades")
print("The square root of your age is", root)