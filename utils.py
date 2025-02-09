import ctypes
import os

def get_dll():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    dll_path = os.path.join(current_dir, "..", "NeuroLib", "out", "build", "x64-debug", "NeuroLib.dll")

    neuro_lib = ctypes.CDLL(dll_path)
    return neuro_lib