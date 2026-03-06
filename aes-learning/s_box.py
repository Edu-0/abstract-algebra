import numpy as np
import abstract_algebra as aa


# Working with matrices in GF(2)
def byte_to_array(byte):
    return np.array(list(byte), dtype=int)


def vet_sum(vet_a, c):
    byte_res = np.zeros(vet_a.shape[0], dtype=int)
    for i in range(vet_a.shape[0]):
        byte_res[i] = vet_a[i] ^ c[i]
    return byte_res


def mat_mul(matA, vet_b):
    vet_res = np.zeros(matA.shape[0], dtype=int)
    for i in range(matA.shape[0]):
        for j in range(vet_b.shape[0]):
            vet_res[i] ^= matA[i][j] & vet_b[j]
    return vet_res


# Affine Transform is the main operation on S-Box, which finds the values equals to the ones on the table
def affine_transform(matA, vet_b, c):
    return vet_sum(mat_mul(matA, vet_b), c)


def arr_to_byte(arr):
    sub_byte = 0
    for i in range(arr.shape[0]):
        sub_byte |= arr[i] << i
    return sub_byte


def table_positions(b):
    # It's relevant to see those 4 bits to locate on the default table given by AES to verify answers
    left_4_bits = (b >> 4) & 0b1111
    right_4_bits = b & 0b1111
    print(f"Left 4 bits: {bin(left_4_bits)} or {hex(left_4_bits)}")
    print(f"Right 4 bits: {bin(right_4_bits)} or {hex(right_4_bits)}")
    print("")


def aes_sbox(b):
    irr = 0b100011011
    yf = aa.multiplicative_inverse(irr, b)

    # Beginning the S-box programming

    mat_a = np.array([
        [1, 0, 0, 0, 1, 1, 1, 1],
        [1, 1, 0, 0, 0, 1, 1, 1],
        [1, 1, 1, 0, 0, 0, 1, 1],
        [1, 1, 1, 1, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 1, 1, 1, 0, 0],
        [0, 0, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 1, 1, 1, 1, 1]
    ], dtype=int)

    c = np.array([1, 1, 0, 0, 0, 1, 1, 0], dtype=int)

    vet_b = byte_to_array(bin(yf)[2::].zfill(8)[::-1])

    byte_res = affine_transform(mat_a, vet_b, c)

    sub_byte = arr_to_byte(byte_res)

    return sub_byte

byte = 0b00100010  # 0b00100010: 2x2 in S-Box = 93

# table_positions(byte)

final_sub_byte = aes_sbox(byte)

print(hex(final_sub_byte))