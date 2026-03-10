import numpy as np
from sympy import ceiling

text1 = "João comeu feijão e não fez bem! ≤, ∞, ±, √"
text2 = "An even longer test text with more than 16 bits, 51"
text = "Olá Mundo"
text3 = "aaaaaaaaaaaaaaaa"


# Simple conversion to binary
def string_to_bin(text):
    return list(text.encode("UTF-8"))


# This function makes sure that the list has a size multiple of 16 for it to be able to divide into blocks of 4x4
def normalize_list(bin_list):
    len_bin_list = len(bin_list)
    missing = 16 - len_bin_list % 16
    if missing == 0:
        missing = 16
    for i in range(missing):
        bin_list.append(missing)
    return bin_list


def array_creator(bin_list):
    array_list = []
    for i in range(0, len(bin_list), 16):
        array_list.append(np.array(np.reshape(bin_list[i:i+16], (4,4)), dtype=int))
    return array_list


bin_list = normalize_list(string_to_bin(text2))
print(array_creator(bin_list))