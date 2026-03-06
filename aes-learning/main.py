import numpy as np
import s_box as sb
import shift_rows as sr
import mix_columns as mc
import add_round_key as ark


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


def add_round_key(bb, round_key):
    return ark.add_round_key(mc.mix_columns(sr.shift_rows(s_box_block(bb))), round_key)


def cryptograph_block(bb, round_key):
    return add_round_key(bb, round_key)


byte_block = np.array(
    [
        [0xEA, 0x04, 0x65, 0x85],
        [0x83, 0x45, 0x5D, 0x96],
        [0x5C, 0x33, 0x98, 0xB0],
        [0xF0, 0x2D, 0xAD, 0xC5]
    ],
    dtype=int
)

test_key = np.array(
    [
        [0xAC, 0x19, 0x28, 0x57],
        [0x77, 0xFA, 0xD1, 0x5C],
        [0x66, 0xDC, 0x29, 0x00],
        [0xF3, 0x21, 0x41, 0x6A]
    ],
    dtype=int
)

ciphered_byte = cryptograph_block(byte_block, test_key)

print_hex(ciphered_byte)