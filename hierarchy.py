#!/usr/bin/python

""" This program is designed as a solution to the BT coding excercise
for Organisation Chart Traversal. 

It is developed to run under Python 2.7"""

__author__ = "Patrick Monaghan (patrick@patrickmonaghan.co.uk)"

import sys
import os.path
from classes import Graph

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
		path_format = path_to_string(graph, path)
		print(path_format)
	else:
		sys.exit("No path was found between %s and %s" % (start, end))
		
def build_graph(filename):
	""" This method takes the text file and builds the graph """
	if not os.path.isfile(filename):
		# If the file does not exist, return nothing
		return None
	
	# Create the graph file
	graph = Graph()
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
		data = [id, name, manager]
		file_data.append(data)
	
	# Now loop through all the data and create nodes. Edges are not added at 
	# this point as we cannot guarantee the order in which we get data in
	for data in file_data:
		id = data[0]
		name = data[1]
		graph.add_node(name, id)
	
	# Now we have all nodes in, we can create the edges
	for data in file_data:
		id = data[0]
		name = data[1]
		manager = data[2]
		graph.add_edge(id, name, manager)
		
	return graph
	
def path_to_string(graph, path):
	""" This method takes the graph and a path between two nodes, and formats
	    the path into the required output format """

	try:
		direction = "->"
		last_manager = None
	
		# Print the first element to start the list
		start = path[0]
		id = graph.node_id(start)
		last_manager = graph.get_manager(id)
		path_string = "%s (%s)" % (start, id)
	
		for node in path[1:]:
			id = graph.node_id(node)
			if id != last_manager:
				direction = "<-"
			last_manager = graph.get_manager(id)
			path_string = "%s %s %s (%s)" % (path_string, direction, node, id)
		
		return path_string
	except:
		# We already know our graph build and find functions are working
		# So an error here indicates no path
		return None
	
if __name__ == "__main__":
	main(sys.argv)