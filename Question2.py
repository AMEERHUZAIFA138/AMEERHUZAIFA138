##Q2) Write a program that prompts the user to enter two floating-point numbers and then calculate their average. 
##The program should display the result with two decimal places.

number1 = float(input( "enter first your number : " ))
number2 = float(input( "enter second your number : "))

# first no is 5.0
# second no is 15.0

#calculate average
average= (number1+ number2)/2
#print
print ("the average is: {:.2f}".format(average))
