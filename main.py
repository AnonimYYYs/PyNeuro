import neuro

import networkx as nx
import matplotlib.pyplot as plt

my_World = neuro.World()
my_World.create_random_world(1, 2, 0.2)

#OSError: exception: access violation reading 0x000000006EEFFD90
my_World.forward_pass()
my_World.print_ions()

# synapse_list = my_World.get_synapses()
#
# # print(f"Number of synapses: {len(synapse_list)}")
# # for synapse in synapse_list:
# #     print(f"Weight: {synapse.weight}, Connected Neurons: {synapse.neuron1_index}-{synapse.neuron2_index}")
#
# edgelist = []
# for synapse in synapse_list:
#     weight_str = "{:.3f}".format(synapse.weight)  # Format to 5 decimal places
#     edgelist.append((synapse.neuron1_index, synapse.neuron2_index, {'weight': weight_str}))
# print (edgelist)
# gWorld = nx.Graph(edgelist)
# print(gWorld)
#
# nIons = my_World.get_ions_size()
# color_map = []
# for node in gWorld:
#     if node <= nIons:
#         color_map.append('#3368ff')
#     else:
#         color_map.append('#8f8f8f')
#
# pos = nx.spring_layout(gWorld)
#
# edge_labels = nx.get_edge_attributes(gWorld, 'weight')
# nx.draw_networkx_edge_labels(gWorld, pos,  edge_labels=edge_labels)
#
# nx.draw(gWorld, pos, node_color=color_map, with_labels=True, font_weight='bold')
# nx.draw_networkx_edge_labels(gWorld, pos, edge_labels=edge_labels)
# plt.show()
#
