""" This program is designed as a  to the BT coding excercise
for Organisation Chart Traversal. 

It is developed to run under Python 2.7"""

__author__ = "Patrick Monaghan (patrick@patrickmonaghan.co.uk)"
import re

class Employee():
	
	""" This class represents an employee in the organisation chart """
	def __init__(self, name="", id=-1, manager_id=-1):
		self.name = name
		self.id = int(id)
		if manager_id:
			self.manager_id = int(manager_id)
		else:
			self.manager_id = None
		
	def set_name(self, name):
		self.name = name
		
	def get_name(self):
		return self.name
		
	def set_id(self, id):
		self.id = int(id)
		
	def get_id(self):
		return self.id
		
	def set_managerid(self, mid):
		self.manager_id = int(mid)
	
	def get_managerid(self):
		return self.manager_id
		
class OrganisationChart():

	def __init__(self):
		self.__employees__ = []
	
	def add_employee(self, emp):
		self.__employees__.append(emp)
		
	def get_employees(self):
		return self.__employees__
		
	def get_employees_by_ids(self, start, end):
		""" This method returns two employee objects based on IDs """
		emps = self.get_employees()
		start_emp = None
		end_emp = None
		
		for emp in emps:
			if emp.get_id() == start:
				start_emp = emp
			if emp.get_id() == end:
				end_emp = emp
		
		return start_emp, end_emp
	
	def get_employee_by_id(self, id):
		""" This method returns an employee object based on a given ID """
		emps = self.get_employees()
		
		for emp in emps:
			if emp.get_id() == id:
				return emp
				
		return None
		
	def get_edges_by_id(self):
		""" This method returns a dictionary, where the employee ID is the 
		key and the manager ID is the value """
		edges = {}
		for emp in self.get_employees():
			edges[emp.get_id()] = emp.get_managerid()
		return edges
		
	def get_nodes(self):
		""" This method returns a dictionary where the employee name is the 
		key and the employee ID is the value """
		nodes = {}
		for emp in self.get_employees():  
			nodes[emp.get_name()] = emp.get_id()
		return nodes
		
	def get_nodes_ids(self):
		""" This method returns a list of employee IDs """
		employees = self.get_employees()
		ids = [int(emp.get_id()) for emp in employees]
		return ids
		
	def get_nodes_and_edges(self):
		""" This method returns a dictionary where the employee ID is the key
		and the edges are a list of values """
		
		nodes = self.get_employees()
		
		# Create the initial dictionary with no values
		edges = {}
		for node in nodes:
			id = node.get_id()
			edges[id] = []
			
		# Now that we have an initial dictionary, we populate it with the edges
		# of the graph. To ensure we have proper data flow, populate the 
		# managers list of edges as well as the current employee
		for node in nodes:
			id = node.get_id()
			mgr_id = node.get_managerid()
			
			# Check that this employee has a manager
			if mgr_id:
				if mgr_id not in edges[id]:
					edges[id].append(mgr_id)
			
				if id not in edges[mgr_id]:
					edges[mgr_id].append(id)
				
		return edges
	
	def format_name(self, name):
		""" This method takes a name and formats it so we can search with it.
		Leading and trailing spaces are removed, multiple spaces are removed
		and the name is cast to uppercase. Doing all comparisons in the one
		case means we are not case sensitive """
		name = str(name).lstrip() # Remove leading spaces
		name = name.rstrip() # Remove trailing spaces
		name = re.sub(' +', ' ', name) # Remove multiple spaces
		return name.upper() # Cast to uppercase
		
	def find_path(self, start, end):
		""" This method takes two names and finds the path between them on the
		organisation chart by calling the recursive find_path_by_ids method """
		
		start = self.format_name(start)
		end = self.format_name(end)
		
		start_id = None
		end_id = None
		
		# Now search the list of employees to get the IDs rather than 
		# names. This allows us to search between two employees who have the
		# same names, but unique IDs.
		employees = self.get_employees()
		for emp in employees:
			empname = emp.get_name()
			empname = self.format_name(empname)
			
			if empname == start:
				# We have found our start employee ID
				start_id = emp.get_id()
			elif empname == end:
				# We do if/else to ensure we get different employees even if
				# they have the same name
				end_id = emp.get_id()
				
		
		if start_id and end_id:
			path = self.find_path_by_ids(start_id, end_id)
			if not path:
				return None
			else:	
				return path
		else:
			return None
			
	def find_path_by_ids(self, start, end, path=[]):
		""" This recursive method finds the path between two employee IDs """
		
		path = path + [start]
		start_emp, end_emp = self.get_employees_by_ids(start, end)
		nodes = self.get_nodes_ids()
		edges = self.get_nodes_and_edges()
		
		
		if start == end:
			# If the start and end nodes are the same, we've reached the
			# end of the 
			
			# Setup the start of the string
			direction = "->"
			last_manager = None
			start = path[0]
			emp = self.get_employee_by_id(start)
			last_manager = emp.get_managerid()
			path_string = "%s (%s)" % (emp.get_name(), emp.get_id())
			
			# For each subsequent employee, build a formatted string
			for node in path[1:]:
				emp = self.get_employee_by_id(node)
				if node != last_manager:
					# If this node has a different ID from the previous nodes
					# manager ID, then we have reached the peak and started
					# descending the chart again: the current node is not the
					# manager of the previous node
					direction = "<-"
				last_manager = emp.get_managerid()
				path_string = "%s %s %s (%s)" % (path_string, direction,
					emp.get_name(), emp.get_id())
			return path_string
			
		if start not in nodes:	
			# Specified start node does not exist
			return None
	
		if end not in nodes:
			# Specified end node does not exist
			return None
				
		
		for node in edges[start]:
			if node not in path:
				newpath = self.find_path_by_ids(node, end, path)
				if newpath:
					# We have found a new path, return it
					return newpath
					
		# And if no path is found, return nothing
		return None	