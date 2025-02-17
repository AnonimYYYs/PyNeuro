import utils
import ctypes

import networkx as nx

functions = {
    "World_new": {"argtypes": [], "restype": ctypes.c_void_p},
    "World_delete": {"argtypes": [ctypes.c_void_p], "restype": None},
    "World_createRandomWorld": {"argtypes": [ctypes.c_int, ctypes.c_int, ctypes.c_float], "restype": ctypes.c_void_p},
    "World_printIons": {"argtypes": [ctypes.c_void_p], "restype": None},
    "World_getSynapsesSize": {"argtypes": [ctypes.c_void_p], "restype": ctypes.c_size_t},
    "World_getSynapses": {"argtypes": [ctypes.c_void_p, ctypes.c_int], "restype": ctypes.c_void_p},
    "World_getSynapseWeight": {"argtypes": [ctypes.c_void_p, ctypes.c_int], "restype": ctypes.c_double},
    "World_getSynapseConnectedNeuron1": {"argtypes": [ctypes.c_void_p, ctypes.c_int], "restype": ctypes.c_int},
    "World_getSynapseConnectedNeuron2": {"argtypes": [ctypes.c_void_p, ctypes.c_int], "restype": ctypes.c_int},
    "World_getIonsSize": {"argtypes": [ctypes.c_void_p], "restype": ctypes.c_int},
    "World_checkIfIon": {"argtypes": [ctypes.c_void_p, ctypes.c_int], "restype": ctypes.c_bool},
    "World_createSmallWorld": {"argtypes": [ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_float], "restype": ctypes.c_void_p}
}

neuro_lib = utils.get_dll(functions)





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

    def create_graph(self):
        print("test")
        edgelist = []
        for i in range(0, self.get_synapses_size()):
            edgelist.append((self.get_synapse_neuron1(i), self.get_synapse_neuron2(i), {'weight': "{:.3f}".format(self.get_synapse_weight(i))}))
            #edgelist.append((self.get_synapse_neuron1(i), self.get_synapse_neuron2(i)))
        print(edgelist)
        self.world_graph = nx.Graph(edgelist)
        return self.world_graph

    def create_small_world(self, nIons, nNeurons, degree, rewire):
        if self.ptr:
            neuro_lib.World_delete(self.ptr)
        rewire = ctypes.c_float(rewire)
        self.ptr = neuro_lib.World_createSmallWorld(nIons, nNeurons, degree, rewire)