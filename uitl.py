import numpy as np
from PIL import Image

def PalletteToPNG(arrry):
    c_array = np.asarray(arrry)

    array = np.zeros([100, len(c_array) * 100, 3], dtype=np.uint8)
    for x in range(len(c_array)):
        y = x * 10
        array[:, x * 100:] = c_array[x]  # Orange left side

    img = Image.fromarray(array)

    return img

def ColorToPNG(arrry):
    c_array = np.asarray(arrry)
    array = np.zeros([100, 100, 3], dtype=np.uint8)
    array[:, :100] = c_array  # Orange left side
    img = Image.fromarray(array)

    return img