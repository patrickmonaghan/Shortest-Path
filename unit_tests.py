#!/usr/bin/python

"""These are the unit tests for the solution to the BT coding excercise
for Organisation Chart Traversal. 

Developed to run under Python 2.7"""

__author__ = "Patrick Monaghan (patrick@patrickmonaghan.co.uk)"

import hierarchy
import unittest

class SolutionCheck(unittest.TestCase):
	filename = "superheroes.txt"
	
	def testSolutionExampleWorks(self):
		"""Check that the given example works"""
		start = "Batman"
		end = "Super Ted"
		expected = "Batman (16) -> Black Widow (6) -> Gonzo the Great (2) -> Dangermouse (1) <- Invisible Woman (3) <- Super Ted (15)"
		
		graph = hierarchy.build_graph(self.filename)
		path = graph.find_path(start, end)
		path_format = hierarchy.path_to_string(graph, path)
		self.assertEquals(expected, path_format)
		
	def testSolutionWorks(self):
		"""Check that another example works"""
		start = "Catwoman"
		end = "Dangermouse"
		expected = "Catwoman (17) -> Black Widow (6) -> Gonzo the Great (2) -> Dangermouse (1)"
		
		graph = hierarchy.build_graph(self.filename)
		path = graph.find_path(start, end)
		path_format = hierarchy.path_to_string(graph, path)
		self.assertEquals(expected, path_format)
		
		
if __name__ == "__main__":
    unittest.main()
