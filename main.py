from neuro.Network import Network
from neuro.Network.SimpleForwardNetwork import SimpleForwardNetwork
import networkx as nx
import matplotlib.pyplot as plt

my_Network = Network()
#my_Network.create_random_world(5, 5, 0.2)
my_Network.create_small_world(5,8,2,0.3)

my_ForwardNetwork = SimpleForwardNetwork()
my_ForwardNetwork.create_new_network(my_Network)

my_ForwardNetwork.forward_pass()
my_Network.print_ions()

graph = my_Network.create_graph()

color_map = []
for node in graph:
    if my_Network.check_if_ion(node):
        color_map.append('#3368ff')
    else:
        color_map.append('#8f8f8f')

#pos = nx.spiral_layout(graph)
pos = nx.circular_layout(graph)

edge_labels = nx.get_edge_attributes(graph, 'weight')
nx.draw_networkx_edge_labels(graph, pos,  edge_labels=edge_labels)

nx.draw(graph, pos, node_color=color_map, with_labels=True, font_weight='bold')
nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)
plt.show()

