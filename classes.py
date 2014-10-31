class Graph():
	
	def __init__(self):
		""" This method is called when a graph object is 
			initialized """
		# Create a private dictionary for the graph
		self.__graph__ = {}
		# Create a private dictionary for mapping names to IDs
		self.__name_mapping__ = {}
		# Create a private dictionary for mapping IDs to names
		self.__id_mapping__ = {}
		
		
	def add_node(self, name, id):
		""" This method adds a node to the graph and notes the ID of the node
		    for mapping IDs to names. Edges are not added at this point """
		if name not in self.__graph__:
			# If the name doesn't already exist in the graph, add it as a 
			# node
			self.__graph__[name] = []
		
		if name not in self.__name_mapping__:
			# If the name isn't already mapped to an ID, map it
			self.__name_mapping__[name] = id
		
		if id not in self.__id_mapping__:
			# If the ID isn't already mapped to an ID, map it
			self.__id_mapping__[id] = name

	def add_edge(self, name, manager):
		""" This method adds an edge between nodes, representing an employee
		    and his/her manager """
		# We will receive the manager as an ID, so find the name
		if manager in self.__id_mapping__:
			manager_name = self.__id_mapping__[manager]
		
		# If both the employee and manager exist in the graph, add the edge
		if name in self.__graph__ and manager_name in self.__graph__:
			# Make sure we don't add duplicate edges
			if manager_name not in self.__graph__[name]:
				self.__graph__[name].append(manager_name)
			If name not in self.__graph__[manager_name]:
				self.__graph__[manager_name].append(name)
		