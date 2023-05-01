#!/usr/bin/env python3

"""
File Name: hw2
Description: Homework Code includes a sequential search algorithm, reverse algorithm, selection sort, modified/original quicksort algorithm, insertion sort algorithm and a test case for the quicksort algorithm. 
Author: Freddie Kiessling
Date: April 21, 2023
"""

# Question 2
# (i) Sequential Sort 
# (ii) Function uses the sequential search on the input list 
# (iii) Freddie Kiessling 
# (iv) April 21, 2023 
def sequential_search(lst, target):
	"""
	Perform a sequential search on the given list for the target value.
	Args:
	lst (list): The list to search through.
	target (int): The value to search for.
	Returns:
	int: The index of the target value if it is found, or -1 if it is not
	"""
	
	for i in range(len(lst)): 
		# for loop iterates throught the list
		if target == lst[i]:
		# if statement matches target to 
		# position in list, then returns the position
			return i
		
		elif target < lst[i]:
		# this if statement checks if the target
		# less than the value at te position in
		# the list, and if so it returns -1. 
			return -1
		
	return -1 
		# lastly -1 is printed in te end to 
		# represent that there exists no target
		# value within the input list

# Best Case: The target is the first element, O(1)
# Worst Case: The target is larger than all elements in the list, O(n)
# Average Case: On average, it will go through half the list before it finds the target value or the next item is bigger. O(n/2)


# Question 3
# (i) Reversing elements
# (ii) Function reverses elements in the input list
# (iii) Freddie Kiessling 
# (iv) April 21, 2023 
def reverse(lst):
	"""
	Reverse the elements in the given list.
	Args:
	lst (list): The list to reverse.
	Returns:
	list: A new list with the elements in reverse order.
	"""
	new_lst = [0] * len(lst)
	# this creates a new list the length of lst
	
	for i in range(len(lst)):
	# for loop iterates through lst
		new_lst[i] = lst[-i-1]
	# this reverses the order of items in the list
	return new_lst
	# returns the new list

# Computational Complexity in Big O notation: O(n)

# Question 4
# (i) Selection Sort 
# (ii) Function uses the selection sort on the input list with an optional flag for choosing between ascending and descending modes
# (iii) Freddie Kiessling 
# (iv) April 21, 2023 
def selection_sort(lst, ascending=True):
	"""
	Sort the given list using the selection sort algorithm, with an optional
	flag for choosing between ascending and descending modes.
	Args:
	lst (list): The list to be sorted.
	ascending (bool, optional): If True (default), sort in ascending order.
	If False, sort in descending order.
	Returns:
	list: A new list containing the sorted elements.
	"""
	new_lst = lst.copy()
	# This line creates a new list new_lst that is a copy of the input list lst
	n = len(new_lst)
	# determine the number of elements that need to be sorted
	for i in range(n):
		min_max_i = i
	# variable keeps track of the index of the minimum or maximum element
	# in the unsorted portion of the list, this if the sort is ascending or descending. 
		for j in range(i + 1, n):
			if ascending: 
			# checks for ascending
				if new_lst[j] < new_lst[min_max_i]:
					min_max_i = j
			# this line of code indicates new minimum or maximum value
			else:
				if new_lst[j] > new_lst[min_max_i]:
					min_max_i = j
			# indicates new minimum or maximum value
		new_lst[i], new_lst[min_max_i] = new_lst[min_max_i], new_lst[i]
			# puts the minimum or maximum value in sorted position
	return new_lst
	
# Question 5
# (i) Modified Quicksort
# (ii) Quicksort function so that calls insertion sort to sort any sublist whose size is less than 50 items. 
# (iii) Freddie Kiessling 
# (iv) April 21, 2023 
def modified_quicksort(lst, threshold=50):
	if len(lst) <= 1:
		return lst
	# checks if the length of the list is less than or equal to 1
	# if yes, return the list since it is already sorted.
	
	if len(lst) < threshold:
		return insertion_sort(lst)
	# checks if the length of the list is less than the given 
	# threshold value. If it is then it calls the insertion_sort
	# function to sort the list.
	
	pivot = lst[len(lst) // 2]  #already casts result to an int
		
	left = []
	for x in lst:
		if x < pivot:
			left.append(x)
	middle = []
	for x in lst:
		if x == pivot:
			middle.append(x)
	right = []
	for x in lst:
		if x > pivot:
			right.append(x)
			
			# These code blocks use a loop to iterate over
			# the list and divide it into three sub-lists: left,
			# middle, and right. left contains all the elements less
			#than the pivot, middle contains all elements equal to 
			# the pivot, and right contains all elements greater than the pivot
	
	return modified_quicksort(left) + middle + modified_quicksort(right)
			# combined the sorted left and right
			# sub-lists with the middle pivot values.
			
def insertion_sort(lst):
	for i in range(1, len(lst)):
		# uses a loop to iterate over each element in the input list except 
		# for the first one because there are no elements to its left
		j = i
		while j > 0 and lst[j-1] > lst[j]:  # swaps the values
			temp = lst[j]
			lst[j] = lst[j-1] 
		# j and j-1 are swapped using the temporary variable temp
			lst[j-1] = temp
		# the while loop swaps elements until the current element 
		# is in the correct sorted position in the list. Then the while
		# as loop continues as long as the index j is greater than 0 
		# and the element to its left is greater than the current element.
			j -= 1
	return lst
		# then the sorted list is returned

# Compare original quicksort to modified version
def original_quicksort(lst):
	if len(lst) <= 1:
		return lst
	
	pivot = lst[len(lst) // 2]  #already casts result to an int
	
	left = []
	for x in lst:
		if x < pivot:
			left.append(x)
	middle = []
	for x in lst:
		if x == pivot:
			middle.append(x)
	right = []
	for x in lst:
		if x > pivot:
			right.append(x)
	
	return original_quicksort(left) + middle + original_quicksort(right)
	
	# This code needs no explanation because it is a replica of the
	# modified version for which I commented above.

import random
import time
import sys

def test_quicksort():
	list50 = random.sample(range(0,1000000), 50)
	list500 = random.sample(range(0,1000000), 500)
	list5000 = random.sample(range(0,1000000), 5000)
	
	min_t_50 = 5001
	min_t_500 = 5001 # 5001 is greater than the maximum possible value of tictoc and can be used as a baseline for comparisons
	min_t_5000 = 5001
	
	min_time_50 = sys.maxsize
	min_time_500 = sys.maxsize # sys module is used to set an initial large value for the minimum sorting time.
	min_time_5000 = sys.maxsize
	
	
	for threshold in range(1, 51):
		#print(threshold)
		if threshold <= len(list50):
			tic = time.perf_counter()
			modified_quicksort(list50, threshold)
			toc = time.perf_counter()
			tictoc = toc - tic
			if tictoc < min_time_50:
				min_t_50 = threshold
				min_time_50 = tictoc
				
				
		# This iterates through threshold values from 1 to 50 and it checks if the values are less
		# than or equal to the length of each of the three lists. If it is, it runs the modified_quicksort()
		# function on that list with that value of threshold, and measures the time it takes to run using
		# time.perf_counter(). Then it compares the time taken to the current minimum time for that list length,
		# and thenupdates the minimum time and the value of threshold that produced that minimum time if the
		# current time is smaller. Then it returns the best threshold value for each list length.


		if threshold <= len(list500):
			tic = time.perf_counter()
			modified_quicksort(list500, threshold)
			toc = time.perf_counter()
			tictoc = toc - tic
			if tictoc < min_time_500:
				min_t_500 = threshold
				min_time_500 = tictoc
				
		if threshold <= len(list5000):
			tic = time.perf_counter()
			modified_quicksort(list5000, threshold)
			toc = time.perf_counter()
			tictoc = toc - tic
			if tictoc < min_time_5000:
				min_t_5000 = threshold
				min_time_5000 = tictoc
				
	print(f'50: {min_t_50} 500: {min_t_500} 5000: {min_t_5000}')
	
	# This code is used as a test to test the modified_quicksort() function with various threshold values in order to
	# find the minimum threshold value that produces the fastest sorting time for three different
	# lists of varying lengths. Then prints out the threshold values that produce the fastest
	# sorting times for each list. The random and time modules are used to generate random lists
	# and measure the sorting times. The sys module is used to set an initial large value for the minimum sorting time.
	
import random
import sys
import time

# Find the optimal threshold value for the quicksort algorithm
def find_optimal_threshold(lst):
	threshold = 0
	min_time = sys.maxsize
	for i in range(1, len(lst)):
		start = time.time()
		modified_quicksort(lst, i)
		end = time.time()
		duration = end - start
		if duration < min_time:
			min_time = duration
			threshold = i
			# print(f'New threshold: {threshold}, time: {min_time}')
		elif duration > 2 * min_time:
			# This is going the wrong way so just abort
			# print(f'Aborting at threshold: {i}')
			break
	return threshold

def find_average_threshold(size, reps):
	thresholds = []
	for i in range(reps):
		lst = random.sample(range(1000000), size)
		thresholds.append(find_optimal_threshold(lst))
	# return average threshold
	return sum(thresholds) / len(thresholds)
	

#50: 23 500: 42 5000: 14


if __name__ == "__main__":
	#print(selection_sort([1,5,4,20,6]))
	#test_quicksort()
	print(f'Avg for 50: {find_average_threshold(50, 1000)}')
	print(f'Avg for 500: {find_average_threshold(500, 100)}')
	print(f'Avg for 5000: {find_average_threshold(5000, 10)}')
	
	#Avg for 50: 9.427
	#Avg for 500: 10.46
	#Avg for 5000: 27.5