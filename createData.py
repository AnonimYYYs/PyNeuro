import pandas as pd
import numpy as np
import random

def create_xor():
    num_rows = 1000

    a = np.random.randint(0, 2, num_rows, dtype=bool)
    b = np.random.randint(0, 2, num_rows, dtype=bool)
    c = np.random.randint(0, 2, num_rows, dtype=bool)
    d = np.random.randint(0, 2, num_rows, dtype=bool)

    e = np.logical_xor(a, b)
    f = np.logical_and(e, np.logical_or(c, d))

    df = pd.DataFrame({
        'a': a,
        'b': b,
        'c': c,
        'd': d,
        'e': e,
        'f': f
    })

    df = df.astype(int)

    delimiter = ';'
    df.to_csv('dataset.csv', index=False, sep=delimiter)

    print(f"XOR Dataset 'xor_dataset.csv' created successfully.")


def create_custom_dataset(rows, cols, empty_cell_probability=0.2):

    #датасет со значениями от -10 до 10
    df = pd.DataFrame(np.random.randint(-10, 11, size=(rows, cols)))

    #создаем пустые ячейки
    for i in range(rows):
        for j in range(cols):
            if random.random() < empty_cell_probability:
                df.iloc[i, j] = None

    #проверяем полностью пустые строки
    for i in range(rows):
        if df.iloc[i].isnull().all():
            #если строка полностью пустая, создаем значение для случайной ячейки
            j = random.randint(0, cols - 1)
            df.iloc[i, j] = random.randint(-10, 11)

    delimiter = ';'
    filename = f"{cols}x{rows}_dataset.csv"
    df.to_csv(filename, index=False, sep=delimiter)
    print(f"Custom Dataset {filename} created successfully.")

rows = 100
cols = 10
create_custom_dataset(rows, cols)

