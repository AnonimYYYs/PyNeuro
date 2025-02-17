import ctypes
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
dll_path = os.path.join(current_dir, "..", "NeuroLib", "out", "build", "x64-debug", "NeuroLib.dll")

neuro_lib = ctypes.CDLL(dll_path)

def get_dll(functions = dict()):
    for f_name, f_data in functions.items():
        f = getattr(neuro_lib, f_name)
        f.argtypes = f_data["argtypes"]
        f.restype = f_data["restype"]
    return neuro_lib