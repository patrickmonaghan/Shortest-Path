""" This program is designed as a  to the BT coding excercise
for Organisation Chart Traversal. 

This file provides the custom exceptions

It is developed to run under Python 2.7"""

class EdgesError(Exception):
     def __init__(self, value):
         self.value = value
     def __str__(self):
         return repr(self.value)
	
class InvalidEmployeeID(Exception):
     def __init__(self, value):
         self.value = value
     def __str__(self):
         return repr(self.value)
	
class NonExistentFile(Exception):
     def __init__(self, value):
         self.value = value
     def __str__(self):
         return repr(self.value)
	