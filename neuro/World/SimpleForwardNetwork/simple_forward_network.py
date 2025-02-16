import utils
import ctypes
from neuro.World import World

neuro_lib = utils.get_dll()

functions = {
    "SimpleForwardNetwork_new": {"argtypes": ctypes.c_void_p, "restype": ctypes.c_void_p },
    "SimpleForwardNetwork_delete": {"argtypes": ctypes.c_void_p, "restype": []},
    "SimpleForwardNetwork_ForwardPass": {"argtypes": ctypes.c_void_p, "restype": ctypes.c_void_p}
}

for f_name, f_data in functions.items():
    f = getattr(neuro_lib, f_name)
    f.argtypes = f_data["argtypes"]
    f.restype = f_data["restype"]

class SimpleForwardNetwork:
    def __init__(self):
        self.ptr = None

    def create_new_network(self, world):
        if self.ptr:
            neuro_lib.SimpleForwardNetwork_delete(self.ptr)
        self.ptr = neuro_lib.SimpleForwardNetwork_new(world.ptr)

    def forward_pass(self):
        neuro_lib.SimpleForwardNetwork_ForwardPass(self.ptr)