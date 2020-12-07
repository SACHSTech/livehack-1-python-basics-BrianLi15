----------------------------------------------------------------------
Name:		problem2.py
Purpose:	
Given the number of student and pieces of chicken to distribute, it will find how many pieces of chicken each student will get evenly. Additionally, it will find the amount of chicken Mr. Fabroa will get from the remaining pieces.

Author:	Li.B

Created:	07/12/2020
----------------------------------------------------------------------
#This gets the number of student in the class from user input
number_student = int(input("Input number of student in the class: "))

#This gets the amount of chicken from user input
number_chicken = int(input("Input the number of pieces of chicken: "))

#This finds the amount of chicken each student will recieve evenly
each_student_piece = number_chicken // number_student

#This finds the amount of chicken leftover for Mr. Fabroa
leftover_pieces = number_chicken % number_student

#This prints the amount of chicken each student in the class will get
print("This is the amount of chicken each student will get: " + str(each_student_piece))

#This prints the amount of chicken Mr. Fabroa will get
print("This is the amount of chicken Mr. Fabroa will get: " + str(leftover_pieces))