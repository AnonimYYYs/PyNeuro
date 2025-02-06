
# test.py
import ctypes

dll_path = "../NeuroLib/out/build/x64-debug/NeuroLib.dll"

# Загружаем DLL
neuro_lib = ctypes.CDLL(dll_path)
#World_new
neuro_lib.World_new.argtypes = []
neuro_lib.World_new.restype = ctypes.c_void_p
#World_delete
neuro_lib.World_delete.argtypes = [ctypes.c_void_p]
neuro_lib.World_delete.restype = None
#World_createRandomWorld
neuro_lib.World_createRandomWorld.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_float]
neuro_lib.World_createRandomWorld.restype = ctypes.c_void_p
#World_printIons
neuro_lib.World_printIons.argtypes = [ctypes.c_void_p]
neuro_lib.World_printIons.restype = None

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

