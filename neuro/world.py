import utils
import ctypes
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
        print (self.ptr)

    def get_ions_size(self):
        return neuro_lib.World_getIonsSize(self.ptr)

    # def get_synapses(self):
    #     synapse_array_ptr = neuro_lib.World_getSynapsesData(self.ptr)
    #
    #     size = neuro_lib.World_getSynapsesSize(self.ptr)
    #     synapses = []
    #     #переносим синапсы
    #     for i in range(size):
    #         synapse = cSynapse.from_address(ctypes.addressof(synapse_array_ptr.contents) + i * ctypes.sizeof(cSynapse))
    #         synapses.append(synapse)
    #     return synapses

    def forward_pass(self):
        neuro_lib.World_forwardPass(self.ptr)