import numpy as np
import s_box as sb
import shift_rows as sr
import mix_columns as mc


def print_hex(bb):
    for i in range(bb.shape[0]):
        for j in range(bb.shape[1]):
            print(f"{bb[i, j]:02X}", end=" ")
        print()


def s_box_block(bb):
    res_array = np.zeros((4, 4), dtype=int)
    for i in range(res_array.shape[0]):
        for j in range(res_array.shape[1]):
            res_array[i][j] = sb.aes_sbox(bb[i][j])

    return res_array


def shift_rows(bb):
    return sr.shift_rows(s_box_block(bb))


def mix_columns(bb):
    return mc.mix_columns(sr.shift_rows(s_box_block(bb)))


def get_test_block():
    return state


byte_block = np.array([
    [0xEA, 0x04, 0x65, 0x85],
    [0x83, 0x45, 0x5D, 0x96],
    [0x5C, 0x33, 0x98, 0xB0],
    [0xF0, 0x2D, 0xAD, 0xC5]],
    dtype=int)

state = mix_columns(byte_block)
print_hex(state)