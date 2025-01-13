
# test.py
import ctypes

dll_path = "../NeuroLib/out/build/x64-debug/NeuroLib.dll"

# Загружаем DLL
neuro_lib = ctypes.CDLL(dll_path)

# Объявляем функцию
neuro_lib.neuro_sum.argtypes = [ctypes.c_int, ctypes.c_int]
neuro_lib.neuro_sum.restype = ctypes.c_int


# Используем функцию
result = neuro_lib.neuro_sum(9, 3)
print(result)  # Должно вывести 8