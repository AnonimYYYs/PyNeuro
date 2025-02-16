from neuro.World import World
# from neuro.World.SimpleForwardNetwork import SimpleForwardNetwork
import networkx as nx
import matplotlib.pyplot as plt

my_World = World()
#my_World.create_random_world(5, 5, 0.2)
my_World.create_small_world(5,10,3,0.3)
#
# my_Network = SimpleForwardNetwork()
# my_Network.create_new_network(my_World)
#
# my_Network.forward_pass()
my_World.print_ions()

graph = my_World.create_graph()

color_map = []
for node in graph:
    if my_World.check_if_ion(node):
        color_map.append('#3368ff')
    else:
        color_map.append('#8f8f8f')

pos = nx.spiral_layout(graph)

edge_labels = nx.get_edge_attributes(graph, 'weight')
nx.draw_networkx_edge_labels(graph, pos,  edge_labels=edge_labels)

nx.draw(graph, pos, node_color=color_map, with_labels=True, font_weight='bold')
nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)
plt.show()

