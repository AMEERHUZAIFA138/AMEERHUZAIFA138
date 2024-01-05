## Q1) Write a program that calculates the area of a triangle using the formula A = (b * h) / 2. 
##The program should prompt the user to enter the base and height of the triangle and then display the calculated area.
# user give base and height input
base=float(input("Enter your base value of triangle : "))
height=float(input("Enter your height value of triangle :"))

#base : 2
#height: 4

#calculate area
area= (base * height) / 2

print("the area of a triangle is: ", area)
