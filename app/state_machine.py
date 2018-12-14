import networkx as nx
from networkx.drawing.nx_agraph import graphviz_layout, to_agraph
import pygraphviz as pgv


class StateMachine:

	def __init__(self):
		self.graph = nx.nx.DiGraph()
		self.graph.graph['graph'] = {'rankdir':'TD'}
		self.graph.graph['node'] = {'shape':'circle'}
		self.graph.graph['edges'] = {'arrowsize':'4.0'}

	def add_node(self, node):
		self.graph.add_node(node)

	def reset(self, transitions):
		self.graph.clear()
		self.graph.add_edges_from(transitions)

	def get_edges(self):
		return self.graph.edges()

	def get_nodes(self):
		return self.graph.nodes()

	def generate(self):
		A = to_agraph(self.graph)
		A.layout('dot')
		A.draw('statemachine.png')
