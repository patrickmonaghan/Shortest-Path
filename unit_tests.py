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
		self.assertEquals(expected, path)
		
	def testSolutionWorks(self):
		"""Check that another example works"""
		start = "Catwoman"
		end = "Dangermouse"
		expected = "Catwoman (17) -> Black Widow (6) -> Gonzo the Great (2) -> Dangermouse (1)"
		
		graph = hierarchy.build_graph(self.filename)
		path = graph.find_path(start, end)
		self.assertEquals(expected, path)

class SanityCheck(unittest.TestCase):
	filename = "superheroes.txt"
	
	def testCaseCheck(self):
		"""Check that the solution is not case sensitive"""
		start = "Batman"
		end = "catwoman"
		expected = "Batman (16) -> Black Widow (6) <- Catwoman (17)"
		
		graph = hierarchy.build_graph(self.filename)
		path = graph.find_path(start, end)
		self.assertEquals(expected, path)
		
	def testTrailingLeaderSpace(self):
		"""Check that trailing and leading space is ignored"""
		start = "     Black Widow"
		end = "Dangermouse    "
		expected = "Black Widow (6) -> Gonzo the Great (2) -> Dangermouse (1)"
		
		graph = hierarchy.build_graph(self.filename)
		path = graph.find_path(start, end)
		self.assertEquals(expected, path)
		
	def testMultipleSpaces(self):
		"""Check that multiple spaces are ignored"""
		start = "     Black       Widow"
		end = "Dangermouse    "
		expected = "Black Widow (6) -> Gonzo the Great (2) -> Dangermouse (1)"
		
		graph = hierarchy.build_graph(self.filename)
		path = graph.find_path(start, end)
		self.assertEquals(expected, path)
		
class StabilityCheck(unittest.TestCase):
	
	def testNoPathFound(self):
		"""Check that we gracefully handle when no path is present"""
		filename = "superheroes.txt"
		start = "Black Widow"
		end = "Patrick Monaghan"
		
		graph = hierarchy.build_graph(filename)
		path = graph.find_path(start, end)
		self.assertEquals(None, path)
		
	def testNoPathFormatted(self):
		"""Check that we gracefully handle when no path exists but we try to
		format"""
		filename = "superheroes.txt"
		start = "Black Widow"
		end = "Patrick Monaghan"
		
		graph = hierarchy.build_graph(filename)
		path = graph.find_path(start, end)
		self.assertEquals(None, path)
		
	def testNoFile(self):
		"""Check that if we give the program a non existent file, it 
		gracefully handles it"""
		filename = "should_not_exist.txt"
		start = "Black Widow"
		end = "Batman"
		
		graph = hierarchy.build_graph(filename)
		self.assertEquals(None, graph)
		
	def testExtendedGraph(self):
		"""Try with a bigger dataset"""
		filename = "testing/datasets/extended_dataset.txt"
		start = "Catwoman"
		end = "Superman"
		
		expected = """Catwoman (17) -> Black Widow (6) -> Gonzo the Great (2) -> Dangermouse (1) <- Captain America (19) <- Wolverine (21) <- Hulk (31) <- SpiderMan (25) <- Superman (35)"""
		
		graph = hierarchy.build_graph(filename)
		path = graph.find_path(start, end)
		self.assertEquals(expected, path)
		
	def testInverseSearch(self):
		"""Check that searching the organisation chart in reverse works: for
		example, searching from right to left"""
		filename = "superheroes.txt"
		start = "Catwoman"
		end = "Batman"
		
		expected = "Catwoman (17) -> Black Widow (6) <- Batman (16)"
		graph = hierarchy.build_graph(filename)
		path = graph.find_path(start, end)
		self.assertEquals(expected, path)
		
if __name__ == "__main__":
    unittest.main()
