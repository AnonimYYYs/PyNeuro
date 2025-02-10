import ctypes
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
dll_path = os.path.join(current_dir, "..", "NeuroLib", "out", "build", "x64-debug", "NeuroLib.dll")

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
    "World_getSynapses": {"argtypes": [ctypes.c_void_p, ctypes.c_int], "restype": ctypes.c_void_p},
    "World_getSynapseWeight": {"argtypes": [ctypes.c_void_p, ctypes.c_void_p], "restype": ctypes.c_double},
    "World_getSynapseConnectedNeuron1": {"argtypes": [ctypes.c_void_p, ctypes.c_int], "restype": ctypes.c_int},
    "World_getSynapseConnectedNeuron2": {"argtypes": [ctypes.c_void_p, ctypes.c_int], "restype": ctypes.c_int},
    "World_getIonsSize": {"argtypes": [ctypes.c_void_p], "restype": ctypes.c_int},
    "World_checkIfIon": {"argtypes": [ctypes.c_void_p, ctypes.c_int], "restype": ctypes.c_bool},
    "World_forwardPass": {"argtypes": [ctypes.c_void_p], "restype": None},
}

for f_name, f_data in functions.items():
    f = getattr(neuro_lib, f_name)
    f.argtypes = f_data["argtypes"]
    f.restype = f_data["restype"]




def get_dll():

    return neuro_lib