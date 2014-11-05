#!/usr/bin/python

""" This program is designed as a solution to the BT coding excercise
for Organisation Chart Traversal. 

It is developed to run under Python 2.7"""

__author__ = "Patrick Monaghan (patrick@patrickmonaghan.co.uk)"

import sys
import os.path
from classes import OrganisationChart, Employee

USAGE = "Usage: python2.7 hierarchy.py [File] [Start] [End]"
			 
def main(args):
	""" This is the main method that is called when the app is started """
	# Get the filenames from the arguments
	try:
		filename = args[1]
		start = args[2]
		end = args[3]
	except Exception:
		sys.exit(USAGE)
	
	graph = build_graph(filename)
	if not graph:
		# Graph does not exist, so file is invalid
		sys.exit("%s is not a valid file." % filename)
		
	path = graph.find_path(start, end)
	if path:
		print(path)
	else:
		sys.exit("No path was found between %s and %s" % (start, end))
		
def build_graph(filename):
	""" This method takes the text file and builds the graph """
	if not os.path.isfile(filename):
		# If the file does not exist, return nothing
		return None
	
	# Create the graph file
	orgchart = OrganisationChart()
	# Open the file and loop through the data
	f = open(filename, 'r')
	# Read the column headers
	header = f.readline()

	file_data = []
	for line in f:
		# Split the line into rows
		line_data = line.split("|")
		# Take in the appropriate data, and remove trailing and leading spaces
		id = line_data[1].lstrip().rstrip()
		name = line_data[2].lstrip().rstrip()
		manager = line_data[3].lstrip().rstrip()
		emp = Employee(name, id, manager)
		orgchart.add_employee(emp)
		
	return orgchart
	
if __name__ == "__main__":
	main(sys.argv)