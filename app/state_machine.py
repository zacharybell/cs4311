import networkx as nx
from networkx.drawing.nx_pydot import write_dot

class StateMachine(nx.DiGraph):
	
	def __init__(self, name):
		self._name = name
		

	def generate(self):
		write_dot(self, "graph.dot")


class Transition:

	def __init__(self, source, target):
		self._source = source
		self._target = target

	def edit(source, target):
		self._source = source
		self._target = target
