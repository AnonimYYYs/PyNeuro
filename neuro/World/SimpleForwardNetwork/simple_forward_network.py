import utils
import ctypes
#from neuro.World import World

functions = {
    "SimpleForwardNetwork_new": {"argtypes": [ctypes.c_void_p], "restype": ctypes.c_void_p},
    "SimpleForwardNetwork_delete": {"argtypes": [ctypes.c_void_p], "restype": None},
    "SimpleForwardNetwork_ForwardPass": {"argtypes": [ctypes.c_void_p], "restype": ctypes.c_void_p}
}

neuro_lib = utils.get_dll(functions)


class SimpleForwardNetwork:
    def __init__(self):
        self.ptr = None

    def create_new_network(self, world):
        if self.ptr:
            neuro_lib.SimpleForwardNetwork_delete(self.ptr)
        self.ptr = neuro_lib.SimpleForwardNetwork_new(world.ptr)

    def forward_pass(self):
        neuro_lib.SimpleForwardNetwork_ForwardPass(self.ptr)