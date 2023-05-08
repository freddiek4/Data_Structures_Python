#!/usr/bin/env python3

'''
File Name: Problem 1
Description: program uses stack to determine whether inputs are palindromes
Author: Freddie Kiessling
Date: May 2, 2023
'''

## Write a program that uses a stack to test input strings to determine whether they are palindromes. A palindrome is a sequence of words that reads the same as the sequence in reverse: for example, noon.

class Stack:
	
	#TODO: Remove the "pass" statements and implement each method
	#Add any methods if necesssary
	#DON'T use any builtin stack class to store your items
	
	def __init__(self): # Constructor function
		self.items = []
	def isEmpty(self): # Returns True if the stack is empty or False otherwise
		return self.items == []
	def len(self): # Returns the number of items in the stack
		return len(self.items)
	def peek(self): # Returns the item at the top of the stack
		return self.items[-1]
	def push(self, item): # Adds item to the top of the stack
		self.items.append(item)
	def pop(self): # Removes and returns the item at the top of the stack
		return self.items.pop()
	
	
def palindrome(input_string):
	isPalindrome = False
	#todo: Your work here
	
	# since spaces are of no interest we use the isalnum function to check
	# for alphanumeric characters and then we use the join function as well 
	# to exclude all spaces. This way we get the input in a single string
	input_string = "".join(i for i in input_string if i.isalnum()).lower()
	
	my_stack = Stack() # creates a stack
	for i in input_string:
		my_stack.push(i) # adds each character of the input string to the stack
		
	isPalindrome = True
	#The for loop iterates through the input string that has no spaces now.
	#Each iteration it compares the ith character of the string to the top
	#character of the Stack function 
	for i in input_string:
		if i != my_stack.pop():
			isPalindrome = False
			break
		
	# Return if input_str is palindrome or not
	return isPalindrome



if __name__ == "__main__":
	my_str = "racecar "
	print(palindrome(my_str)) # Correct Output: True
	#todo (optional): Your testing code here
	
	
'''
Functions associated with stack:

Stack data structure follows the last in first out data (LIFO) format
		- first element added to the stack will be at the bottom
		- last element added to the stack will be at the top 

1. push(item): Adds an item to the top of the stack.
2. pop(): Removes and returns the item at the top of the stack.
3. peek(): Returns the item at the top of the stack without removing it.
4. isEmpty(): Returns True if the stack is empty, and False otherwise.
5. len(): Returns the number of items in the stack.
6. isFull(): Returns True if the stack is full, and False otherwise (applies only to fixed-size stacks).
7. clear(): Removes all the items from the stack.
8. copy(): Returns a copy of the stack.
9. search(item): Returns the 1-based position of the item in the stack, with the top element being position 1.



'''
'''
File Name: Problem 2
Description: The method expects an integer index as an argument. Then it removes and return the item in the queue at that position.
Author: Freddie Kiessling
Date: May 2, 2023
'''
	
	
#   When you send a file to be printed on a shared printer, it is put onto a print queue with other jobs. Anytime before your job prints, you can access the queue to remove it. Thus, some queues support a remove operation. Add this method to the queue implementations. The method should expect an integer index as an argument. It should then remove and return the item in the queue at that position (counting from position 0 at the front to position n – 1 at the rear).
	
	
class Queue:	
	'''
	todo: Remove the "pass" statements and implement each method
	Add any methods if necesssary
	DON'T use any builtin queue class to store your items
	'''
	def __init__(self): # Constructor function
		self.items = []
		
	def isEmpty(self): # Returns True if the stack is empty or False otherwise
		return self.items == []
	
	def len(self): # Returns the number of items in the stack
		return len(self.items)
	
	def peek(self): # Returns the item at the top of the stack
		return self.items[0]
	
	
	def add(self, item): # Adds item to the top of the stack
		self.items.append(item)
		
	def pop(self): # Removes and returns the item at the top of the stack
		return self.items.pop(0)
	
	def remove(self, i):	# removes and returns item at the index of the queue
		if i >= len(self.items) or i < 0:
			return None
		else:
			return self.items.pop(i) 
		
if __name__ == "__main__":
	queue = Queue()
	queue.add("Test_1")
	queue.add("Test_2")
	queue.add("Test_3")
	queue.add("Test_4")
	queue.add("Test_5")
	queue.add("Test_6")
	
	print(queue.peek()) 
	print(queue.len())  
	
	removed_item = queue.remove(0)
	print(removed_item)
	print(queue.len())
	print(queue.peek())
	
	# Expected Output: 
	'''
	Test_1
	6
	Test_1
	5
	Test_2
	'''
	
	'''
1. Queues are linear collections. 
2. Insertions are restricted to one end, called the rear, and removals to the other end, called the front. 
3. A queue thus supports a first-in first-out (FIFO) protocol
	'''
	
'''
File Name: Problem 3
Description: ## This code uses combinations of stack and queue operations to convert a stack into a queue which also reverses the order of numbers in the process. 
Author: Freddie Kiessling
Date: May 2, 2023
'''
#Reuse your Queue Implementation from Q2.
class Queue:
	'''
	todo: Remove the "pass" statements and implement each method
	Add any methods if necessary
	DON'T use any builtin queue class to store your items
	'''
	def __init__(self): # Constructor function
		self.items = []
		
	def isEmpty(self): # Returns True if the queue is empty or False otherwise
		return self.items == []
	
	def len(self): # Returns the number of items in the queue
		return len(self.items)
	
	def peek(self): # Returns the item at the front of the queue
		return self.items[0]
	
	def add(self, item): # Adds item to the end of the queue
		self.items.append(item)
		
	def pop(self): # Removes and returns the item at the front of the queue
		return self.items.pop(0)
	
	def removing_item(self, i): # Removes and returns item at the given index of the queue
		if i >= len(self.items) or i < 0:
			return None
		else:
			return self.items.pop(i)
		
		
## This code uses combinations of stack and queue
## operations to reverse the order of elements in
## the original stack. Queues are FIFO, and Stacks are LIFO. 
		
def stackToQueue(stack):
	# original stack is 1, 2 , 3: Stacks are LIFO so it takes the top element which is the last element: 3
	temp_stack = []
	
	while len(stack) > 0:
		temp_stack.append(stack.pop())   # after this command temp stack has 3, 2, 1
		
	queue = Queue() # ne queue
	
	# we want to add elements from the temp stack to the queue
	
	# we have a new queue
	
	# now we need a function that assigns temp stack to queue. Temp stack is LIFO
	
	while len(temp_stack) > 0:
		queue.add(temp_stack.pop()) # pop takes items at the front of the stack which is currently 3, 2, 1 and stacks are LIFO so the top is 1
	# so this reverses the order of elements from the stack 3,2,1 into the queue in order of 1, 2, 3
	# we have to use add here because its a queue
		
		
	# we do steps 1 and 2 again to add it into reverse order
	# first we have to make a new stack 
		
	reverse_stack = []
	
	while not queue.isEmpty(): # here we add the elements back into the Stack
		reverse_stack.append(queue.pop()) # queue is 1,2,3. pop takes the top which is FIFO so 1 so when we add it back to a stack the stack will also be 1,2,3
	
	#we need one more functio  to have a reverse queue
	
	while len(reverse_stack)>0:
		queue.add(reverse_stack.pop()) #reverse stack is 1,2,3 and stacks are LIFO so the first element removed is 3 then 2 then 1 so the queue now contains elements 3,2,1
		
	return queue

if __name__ == "__main__":
	stack = [1, 2, 3]
	res = stackToQueue(stack)
	queue_elements = []
	while not res.isEmpty():
		queue_elements.append(res.pop())
	print(queue_elements) # The output should be [3, 2, 1]


'''
File Name: Problem 4
Description: ## The code checks if an input string that contains varying brackets is balanced or not (meaning has an equal amount of open and closed brackets)
Author: Freddie Kiessling
Date: May 2, 2023
'''
#Reuse your Stack implementation from q1
from collections import deque
class Stack:
	'''
	todo: Remove the "pass" statements and implement each method
	Add any methods if necesssary
	DON'T use any builtin stack class to store your items
	'''
	def __init__(self): # Constructor function
		self.items = []
	def isEmpty(self): # Returns True if the stack is empty or False otherwise
		return self.items == []
	def len(self): # Returns the number of items in the stack
		return len(self.items)
	def peek(self): # Returns the item at the top of the stack
		return self.items[-1]
	def push(self, item): # Adds item to the top of the stack
		self.items.append(item)
	def pop(self): # Removes and returns the item at the top of the stack
		return self.items.pop()
	
def bracketsBalance(input_str, opening_list, closing_list):
	isBalanced = True
	stk = Stack()
	for i in input_str: # i is the variable for bracket/character in the input lists
		if i in opening_list: # this checks in the for loop, if the ith character
							  # is character is an opening bracket then it pushes it onto the stk stack
			stk.push(i)		  # pushing it onto the stk stack
	
		elif i in closing_list: # here if the ith character is a closing bracket
								# this elif statement's first if statement first 
								# checks if the stk stack is empty. If it is empty
								# we know that there is no corresponding opening 
								# bracket and therefore there is a closed bracket
								# but no open bracket so the brackets are not balanced thus we get the isBalanced = False
	
			if stk.isEmpty():
				isBalanced = False
				break			# the break statements here are used to stop the
								# code if this imbalance occurs. 
			elif opening_list.index(stk.peek()) == closing_list.index(i):
				stk.pop()		# the first elif statement runs under the
								# condition that the stk stack is not empty
								# the statement following the elif checks if the top element of the stack matches the ith 
								# closing bracket element. Since the corresponding
								# opening bracket for the ith current closing
								# bracket has been found we remove the opening bracket from the stack by popping it. We have to do this because otherwise the matching opening bracket will still be in the stack and the code will continue to run considereing that the string is unbalanced
				
			else:				# this else statement is used for the case in 
								# which top element does not match showing that
								# the brackets are not considered balanced so isBalanced will be False and the loop is halted
				isBalanced = False
				break
	if not stk.isEmpty():		# we need this code chunk after the loop is done
								# to check if the stack is empty, we do this to 
								# check if there are any opening brackets left in the stack. Because if there are opening brackets left in the stack we know that the brackets are not balanced so isBalanced is set to False. 
		isBalanced = False
	return isBalanced

	
if __name__ == "__main__":
	my_str = "([{))}"
	opening_list=['(', '[', '{']
	closing_list=[')', ')', '}']
	print(bracketsBalance(my_str,opening_list,closing_list)) # Correct Output:
False
	#todo (optional): Your testing code here
	
	
'''
File Name: Problem 5
Description: ## The code implements a simple linked list in Python and has the capacity to create a sequence of nodes and construct a linear linked list, insert a new node in the linked list, delete a particular node in the linked list, modify the linear linked list into a circular linked list.
Author: Freddie Kiessling
Date: May 2, 2023
'''


# Please don't change any function names
# Node implementation provided! Don't touch it.
class Node:
	def __init__(self, val=None):
		self.val = val
		self.next = None
class LinkedList:
	"""
	todo: Remove the "pass" statements and implement each method
	Add any methods if necessary
	DON'T use a builtin list to keep all your nodes.
	"""
	def __init__(self):
		self.head = None # The head of your list, don't change its name. It should be "None" when the list is empty.
		
		
	## The append function appends the num to the tail
	## of the list given two scenarios
	def append(self, num): # append num to the tail of the list
		if not self.head:			# if the linked list is not empty we set
			self.head = Node(num)   # the node equal to the head of the list
		else:
			current_node = self.head
			while current_node.next:				# this while loop runs until there
				current_node = current_node.next	# there is a node that has a next
			current_node.next = Node(num)			# pointer that is None.
													# Now, at the end of the list we 
													# create a new node that has the
													# pointer of the last node pointed
													# at it.
			
			
	def insert(self, index, num): # insert num into the given index
		new_created_node = Node(num)
		
		## two scenarios here: 1) if the index is 0 and 2) if it is not 0
		## If the index is 0 we insert the new node at the beginning of 
		## the linked list
		if index == 0:
			new_created_node.next = self.head
			self.head = new_created_node
			
		## In the else statement we traverse the list up until a point 
		## where we find the node that exists at the index or in another
		## scenario the end of the list. 
		else:
			previous_node = None
			current_node = self.head
			count = 0
			
			## this while loop runs until 1) we have reached the desired
			## index or 2) we are out of the index bound of the list/the
			## end of the list
			while current_node and count < index:
				
				## as we traverse through the list
				## the status between current node and 
				## previous node changes so when we loop
				## through we need to set previous node
				## equal to current node
				previous_node = current_node
				
				## with the previous line since now the
				## current node has been updated to the 
				## previous node we set the current node
				## equivalent to the next node
				current_node = current_node.next
				
				
				## the count is updated each loop
				## so that we can keepm track of
				## the nodes that have been traversed through
				count += 1
				
				
			## In this scenario we have reached the end of the list 
			## before reaching the desired index
				
			if count < index:
				raise IndexError("Index out of range")
				
			## This is the final code in which we inster the new
			## node between the previous and current node that
			## we are on. 
				
			new_created_node.next = current_node
			previous_node.next = new_created_node
			
	def delete(self, index): # remove the node at the given index and return the deleted value as an integer
		
		## checks if list is empty. If so, there is an IndexError
		## because there is no node present at the index given.
		
		if not self.head:
			raise IndexError("Index out of range")
			
		## this is in the case of deleting the first node
		## we set the head node to its next node and
		## it returns the deleted head value
		if index == 0:
			deleted_value = self.head.val
			self.head = self.head.next
			
		## if the node is not the head node this code runs
		else:
			
			## this is the set up for the while statement
			## here the previous node is assigned to the head
			## and the current node is assigned to the node 
			## after the head node, and the count is set equal to 1
			previous_node = self.head
			current_node = self.head.next
			count = 1
			
			## while loop runs while the current node and count are
			## less than the index
			while current_node and count < index:
				
				## continously updates the current node to the previous
				## node and sets the current node to the next node
				previous_node = current_node
				current_node = current_node.next
				
				## the count is incremented by 1
				count += 1
				
			## this is for the case that the index is out of range
			## here the error message shows up 
			if not current_node:
				raise IndexError("Index out of range")
				
			# sets the value of the deleted node equal to the deleted value variable
			deleted_value = current_node.val
			# this deletes the node as it is skipping over the deleted node
			previous_node.next = current_node.next
			
		## this is where the deelted node is returned
		return deleted_value
	
	
	def circularize(self): # Make your list circular. This method can only be the last call of the autograder.
		## current node is assigned to the head of the list
		current_node = self.head
		## this while loop runs as long as there is a next node
		## that exists in the linked list
		while current_node.next:
			## the current node is upated tto the next node in the linked list
			current_node = current_node.next
			## this last line is what makes the linked list circular
			## it does so by setting the last node in the linked list
			## equal to the head of the linked list
		current_node.next = self.head
			## by making the last node point to the first node
			## we create a circularity, so there is essentially
			## no end of the listm by starting from any node
			## it will loop back to the beginning of the list
		
if __name__ == "__main__":
	my_list = LinkedList() # []
	my_list.insert(0, 32) # [32]
	my_list.append(-5) # [32, -5]
	my_list.append(19) # [32, -5, 19]
	my_list.insert(1, 6) # [32, 6, -5, 19]
	my_list.delete(2) # [32, 6, 19]
	my_list.circularize()
	
