#!/usr/bin/env python3

#(i) Problem 1 (ii) takes the radius of a sphere (a floating-point number) as input and outputs the sphere’s diameter, circumference, surface area, and volume (iii) Freddie Kiessling (iv) April 11, 2023.
import math #importing math in python to use the math.pi

def sphere(radius):
	
	#calculation of the diameter,circumference,surface area, and volume:
	diameter = 2 * radius 
	circumference  = 2 * math.pi * radius
	surface_area = 4 * math.pi * (radius ** 2)
	volume = (4/3) * math.pi * (radius ** 3)
	
	list_return = [diameter, circumference, surface_area, volume] # puts the calculations into a list
	
	return list_return

radius = 3.5
result = sphere(radius)

print("Diameter:", result[0])
print("Circumference:", result[1])
print("Surface Area:", result[2])
print("Volume:", result[3])


#(i) Problem 2 (ii) program that lets the user enter the initial height of the ball and the number of times the ball is allowed to continue bouncing. Output should be the total distance traveled by the ball (iii) Freddie Kiessling (iv) April 11, 2023.

def bounce(height, bounce_index, num_of_bounce):
	
	distance = height #set distance to height
	
	for i in range(num_of_bounce-1):
		height *=bounce_index
		distance += 2*height
	# for loop incorporates the number of bounces that will be inputed
	# height is multiplied and set equal to the heigh index the distance 
	# is set equal to the height multiplied by 2 because the ball bounces
	# up and down so we have to account for both instances for example when the ball bounces 6 ft high off the ground,
	# the 6ft coming down to the ground must also be accounted for. 
		
		
	distance += height*bounce_index # the height calculated by the bounce index is added to the distance to calculate the total distance value that the ball is travelling
	
	return distance

#(i) Problem 3 (ii) function has an input value of n and approximates the Leibniz series to pi, so the larger n gets the closer the value will approximate pi (iii) Freddie Kiessling (iv) April 11, 2023.



def get_pi(n):
	approximated_value = 0
	term = 0
	# start with term, approximated value as 0.
	
	for i in range(0,n):
		term = (((-1)**i)/((2*i)+1))
		approximated_value += term
	# for loop runs from 0 to the input value of n, while it is incrementing the i value
	# the function that is set equal to the term is representative of the Leibniz series
	# as i increments the term is calculated for each increment of i, and adds it to the approximated value.
		
		
	return approximated_value * 4 # the approximated value is multiplied by 4 to display the approximated value of pi



# (i) Problem 4 (ii) code starts with input of purchase price, then calculates a payment schedule for the lifetime of the loan for computer purchases with various
# conditions such as a 10% down payment, annual interest rate of 12%, and Monthly payments are 5% of the listed purchase price minus the down payment(iii)
# Freddie Kiessling (iv) April 11, 2023.

# input of purchase price assigned to the balance
balance = float(input("Enter purchase price: "))

balance *= 0.9 # 10% down payment
payment = 0.05 * balance # monthly payments of 5%

print(f'Month Balance    Interest   Principal  Payment   New Balance')

month = 1 # first month

while (balance > 0): 
	
	# the while loop is implemented to keep the calculations running until the balance is at 0,
	# this signifies the lifetime of the loan. 
	if (balance <= payment):
		interest = 0
		principal = balance 
		payment = balance
		new_balance = 0
	# runs if balance is less than the payment, sets interest and the new balance equal to 0 
	# to keep it updated and sets principal as well as payment to the balance
		
	else:
		interest = 0.01 * balance # accounting for the annual interest rate of 12%, thus monthly is 12/12 =1
		principal = payment - interest # the principal is calculated by subtracting the payment amount and interest incorporated which is calculated by 1% of balance
		new_balance = balance - principal # this calculates the balance after deducting the principal
	print(f'{month:5d} {balance:10.2f} {interest:10.2f} {principal:10.2f} {payment:10.2f} {new_balance:10.2f}')
	month += 1 # incrementing month
	balance = new_balance # setting balance to new balance to keep the program updated
	
	

#(i) Problem 5 (ii) function merges two sorted lists together into a merged list (iii) Freddie Kiessling (iv) April 11, 2023.
	
	
def merge(list1, list2):
# function takes two lists as input values
	
	if not list1:
		return list2
	
	if not list2:
		return list1
	
	# In this Base Case, these two cases check for the case in which 
	# the list1 or list2 is empty thus it prints the other list so when
	# list1 is empty the merged list will consist of only list 2, 
	# and vice versa
	
	# This is the Recursive case which checks the first elements of both lists.
	if list1[0] < list2[0]:
		
		# If the first element of list1 is smaller than the first element of list2,
		# it will be added to the merged list and then it recursively calls the merge
		# function again with the elements left of list1 and list2.
		return [list1[0]] + merge(list1[1:], list2)
	else:
		# If the first element of list2 is smaller or equal to the first element of list1, 
		# it will be added to the merged list and then it recursively calls the merge
		# function again with the elements left of list1 and list2.
		return [list2[0]] + merge(list1, list2[1:])
	
	
	# Time complexity: O(n) because it is adding elements to the merge list one at a time. 
	# The total number of operations is the length of list 1 + length of list 2, so O(n),
	# where n is the total number of elements that are in both list1 and list2.
	
	
	
#(i) problem_6 (ii) function uses recursion to find the gcd of two postive integers (iii) Freddie Kiessling (iv) April 11, 2023.
	
	
def recursive_gcd(int1, int2):
		# function takes two positive integer input values
	
	if int2 == 0:  
		return int1
		# This is checking the Base case: int2 = 0, so it returns int1
	
	else:
		# here the recursion call happens: when the second integer is not
		# equivalent to 0, the function is called again but this time with int2 
		# int the place of int1 and the remainder of int1 divided by int2 in place of int2
		
		return recursive_gcd(int2, int1 % int2)
	
		# In the case integer 1 is 10, and integer 2 is 5
		# the recursion call will call the function with 5 in
		# the place of int1 and 0 in the place of int2
		# Then when the function is called the if statement is called
		# because int2 = 0, which returns int1 which is 5.
		# We know this to hold true as the gcd of 10, 5 is 5. 
	
		# The function continues to run until int2 = 0. 
	
	
		# The computational time complexity follows the Euclidean algorithm is O(log min(a, b)), 
		# in which a and b are defined as the two positive input integers: int1 and int2.
	
		# The modulo operation is repeatdely called until the second input integer becomes zero. 
		# Becauae the code is assigning the int2 to the remainder of division of int1 and int2,
		# it can be assumed that int2 is decreasing in each step by a factor of 2.
		# This is where I am getting log2(min(a, b)) as my time complexity.
	
		# The time complexity also provides us with the information that the function can
		# be considered an efficient algorithm in finding the GCD of two positive integers.
	
	
	
	
	
	