#Queue Import Module
import Queue 

q = Queue.Queue()

#Stack Implementation
class Stack:
	def _init_(self):
		self.items = []
	
	def push(self, number):
		self.items.append(number)

	def pop(self):
		return self.items.pop()

	def checkSize(self):
		return len(self.items)
#Loic Guegan Assignment 1 Submission
#Stack is in stack.py
#Queue is is queue.py
#Binary tree is in bintree.py
#Graph is in graph.py	
