import utils
import ctypes

import networkx as nx

neuro_lib = utils.get_dll()

functions = {
    "Network_new": {"argtypes": [], "restype": ctypes.c_void_p},
    "Network_delete": {"argtypes": [ctypes.c_void_p], "restype": None},
    "Network_createRandomNetwork": {"argtypes": [ctypes.c_int, ctypes.c_int, ctypes.c_float], "restype": ctypes.c_void_p},
    "Network_printIons": {"argtypes": [ctypes.c_void_p], "restype": None},
    "Network_getSynapsesSize": {"argtypes": [ctypes.c_void_p], "restype": ctypes.c_size_t},
    "Network_getSynapses": {"argtypes": [ctypes.c_void_p, ctypes.c_int], "restype": ctypes.c_void_p},
    "Network_getSynapseWeight": {"argtypes": [ctypes.c_void_p, ctypes.c_int], "restype": ctypes.c_double},
    "Network_getSynapseConnectedNeuron1": {"argtypes": [ctypes.c_void_p, ctypes.c_int], "restype": ctypes.c_int},
    "Network_getSynapseConnectedNeuron2": {"argtypes": [ctypes.c_void_p, ctypes.c_int], "restype": ctypes.c_int},
    "Network_getIonsSize": {"argtypes": [ctypes.c_void_p], "restype": ctypes.c_int},
    "Network_checkIfIon": {"argtypes": [ctypes.c_void_p, ctypes.c_int], "restype": ctypes.c_bool},
    "Network_createSmallWorldNetwork": {"argtypes": [ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_float], "restype": ctypes.c_void_p}
}

for f_name, f_data in functions.items():
    f = getattr(neuro_lib, f_name)
    f.argtypes = f_data["argtypes"]
    f.restype = f_data["restype"]

class Network:
    def __init__(self):
        self.ptr = None

    def delete_world(self):
       if self.ptr:
         neuro_lib.Network_delete(self.ptr)
         self.ptr = None

    def __del__(self):
        self.delete_world()

    def create_new_world(self):
        if self.ptr:
            neuro_lib.Network_delete(self.ptr)
        self.ptr = neuro_lib.Network_new()

    def create_random_world(self, nIons, nNeurons, connect):
        if self.ptr:
            neuro_lib.Network_delete(self.ptr)
        connect = ctypes.c_float(connect)
        self.ptr = neuro_lib.Network_createRandomWorldNetwork(nIons, nNeurons, connect)

    def print_ions(self):
        neuro_lib.Network_printIons(self.ptr)

    def get_ions_size(self):
        return neuro_lib.Network_getIonsSize(self.ptr)

    def get_synapses_size(self):
        return neuro_lib.Network_getSynapsesSize(self.ptr)

    def get_synapses(self):
        self.synapses = []
        n = self.get_synapses_size()
        for i in range (0,n):
            self.synapses.append(neuro_lib.Network_getSynapses(self.ptr, i))
        return self.synapses

    def get_synapse_weight(self, pos):
        return neuro_lib.Network_getSynapseWeight(self.ptr, pos)

    def get_synapse_neuron1(self, pos):
        return neuro_lib.Network_getSynapseConnectedNeuron1(self.ptr, pos)

    def get_synapse_neuron2(self, pos):
        return neuro_lib.Network_getSynapseConnectedNeuron2(self.ptr, pos)

    def check_if_ion(self, index):
        return neuro_lib.Network_checkIfIon(self.ptr, index)

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
            neuro_lib.Network_delete(self.ptr)
        rewire = ctypes.c_float(rewire)
        self.ptr = neuro_lib.Network_createSmallWorldNetwork(nIons, nNeurons, degree, rewire)