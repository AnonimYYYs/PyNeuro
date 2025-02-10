import utils
import ctypes

import networkx as nx

neuro_lib = utils.get_dll()

class World:
    def __init__(self):
        self.ptr = None

    def delete_world(self):
       if self.ptr:
         neuro_lib.World_delete(self.ptr)
         self.ptr = None

    def __del__(self):
        self.delete_world()

    def create_new_world(self):
        if self.ptr:
            neuro_lib.World_delete(self.ptr)
        self.ptr = neuro_lib.World_new()

    def create_random_world(self, nIons, nNeurons, connect):
        if self.ptr:
            neuro_lib.World_delete(self.ptr)
        connect = ctypes.c_float(connect)
        self.ptr = neuro_lib.World_createRandomWorld(nIons, nNeurons, connect)

    def print_ions(self):
        neuro_lib.World_printIons(self.ptr)

    def get_ions_size(self):
        return neuro_lib.World_getIonsSize(self.ptr)

    def get_synapses_size(self):
        return neuro_lib.World_getSynapsesSize(self.ptr)

    def get_synapses(self):
        self.synapses = []
        n = self.get_synapses_size()
        for i in range (0,n):
            self.synapses.append(neuro_lib.World_getSynapses(self.ptr, i))
        return self.synapses

    def get_synapse_weight(self, pos):
        return neuro_lib.World_getSynapseWeight(self.ptr, pos)

    def get_synapse_neuron1(self, pos):
        return neuro_lib.World_getSynapseConnectedNeuron1(self.ptr, pos)

    def get_synapse_neuron2(self, pos):
        return neuro_lib.World_getSynapseConnectedNeuron2(self.ptr, pos)

    def check_if_ion(self, index):
        return neuro_lib.World_checkIfIon(self.ptr, index)

    def forward_pass(self):
        neuro_lib.World_forwardPass(self.ptr)

    def create_graph(self):
        print("test")
        edgelist = []
        for i in range(0, self.get_synapses_size()):
            edgelist.append((self.get_synapse_neuron1(i), self.get_synapse_neuron2(i),
                             {'weight': "{:.3f}".format(self.get_synapse_weight(i))}))
        print(edgelist)
        self.world_graph = nx.Graph(edgelist)
        return self.world_graph
