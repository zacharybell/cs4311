import networkx as nx
import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.pyplot as plt
import pydot
from networkx.drawing.nx_pydot import write_dot

class state_machine(DiGraph):

	__init__(self, name):
		self.name = name
		self.graph = nx.DiGraph()

	def generate(self):
		write_dot(g, "graph.dot")

# g = nx.DiGraph()
# g.add_nodes_from(["type 1", "type 2"])
# g.add_edge("type 1","type 2")
# options = {
#      'node_color': 'blue',
#      'node_size': 100,
#      'width': 3,
#      'arrowstyle': '-|>',
#      'arrowsize': 12,
# }
# nx.draw_networkx(g, arrows=True, **options)
# write_dot(g, "dot.dot")