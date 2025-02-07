
# test.py
import ctypes

dll_path = "../NeuroLib/out/build/x64-debug/NeuroLib.dll"

# Загружаем DLL
neuro_lib = ctypes.CDLL(dll_path)

class cSynapse(ctypes.Structure):
    _fields_ = [("neuron1_index", ctypes.c_int), ("neuron2_index", ctypes.c_int), ("weight", ctypes.c_double)]

#функции из DLL
functions = {
    "World_new": {"argtypes": [], "restype": ctypes.c_void_p},
    "World_delete": {"argtypes": [ctypes.c_void_p], "restype": None},
    "World_createRandomWorld": {"argtypes": [ctypes.c_int, ctypes.c_int, ctypes.c_float], "restype": ctypes.c_void_p},
    "World_printIons": {"argtypes": [ctypes.c_void_p], "restype": None},
    "World_getSynapsesSize": {"argtypes": [ctypes.c_void_p], "restype": ctypes.c_size_t},
    "World_getSynapsesData": {"argtypes": [ctypes.c_void_p], "restype": ctypes.POINTER(cSynapse)},
    "World_getIonsSize": {"argtypes": [ctypes.c_void_p], "restype": ctypes.c_int},
    "World_forwardPass": {"argtypes": [ctypes.c_void_p], "restype": None}
}
#int World_getIonsSize(World* world)
for f_name, f_data in functions.items():
    f = getattr(neuro_lib, f_name)
    f.argtypes = f_data["argtypes"]
    f.restype = f_data["restype"]

class World:
    def __init__(self):
        self.ptr = None

    def __del__(self):
        neuro_lib.World_delete(self.ptr)

    def create_new_world(self):
        self.ptr = neuro_lib.World_new()

    def create_random_world(self, nIons, nNeurons, connect):
        if self.ptr:
            neuro_lib.World_delete(self.ptr)
        self.ptr = neuro_lib.World_createRandomWorld(nIons, nNeurons, connect)

    def print_ions(self):
        neuro_lib.World_printIons(self.ptr)

    def get_ions_size(self):
        return neuro_lib.World_getIonsSize(self.ptr)

    def get_synapses(self):
        synapse_array_ptr = neuro_lib.World_getSynapsesData(self.ptr)

        size = neuro_lib.World_getSynapsesSize(self.ptr)
        synapses = []
        #переносим синапсы
        for i in range(size):
            synapse = cSynapse.from_address(ctypes.addressof(synapse_array_ptr.contents) + i * ctypes.sizeof(cSynapse))
            synapses.append(synapse)
        return synapses

    def forward_pass(self):
        neuro_lib.World_forwardPass(self.ptr)