import numpy as np


def gf_mul(f, g):
    result = 0
    for i in range(g.bit_length()):
        if (g >> i) & 1:
            temp = f
            for _ in range(i):
                of = bin((temp & 0x80) >> 7)[2:]
                temp = (temp << 1) & 0xFF
                if of == "1":
                    temp ^= 0b11011

            result ^= temp
    return result


def gf2_mul(f, g):
    result = 0
    for i in range(g.bit_length()):
        if (g >> i) & 1:
            temp = f
            for _ in range(i):
                temp = temp << 1
            result ^= temp
    return result


def deg(b):
    for i in range(len(bin(b)[2:]) - 1, -1, -1):
        if (b >> i) & 1:
            return i
    return 0


def gf2_div(a, b):
    q = 0
    r = a

    while deg(r) >= deg(b):
        shift = deg(r) - deg(b)
        q |= (1 << shift)
        r ^= (b << shift)
        if r == 0:
            break
    return q, r


def gf_egcd(a, b):
    if b == 0:
        return a, 1, 0

    q, r = gf2_div(a, b)
    g, x1, y1 = gf_egcd(b, r)

    x = y1
    y = x1 ^ gf_mul(q, y1)

    return g, x, y


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


irr = 0b100011011
a = 0b00100010
g, xf, yf = gf_egcd(irr, a)

g_bin, xf_bin, yf_bin = bin(g), bin(xf), bin(yf)
print(f"ax + by = gcd(a, b) -> {bin(irr)}*{xf_bin} + {bin(a)}*{yf_bin} = {g_bin}")

multiplicative_inverse = yf

print("The multiplicative inverse of the given polynom is: ")
print(f"Full value: {bin(yf)} or {hex(yf)}\n")

# Beginning the S-box programming

# It's relevant to see those 4 bits to locate on the default table given by AES to verify answers
left_4_bits = (a >> 4) & 0b1111
right_4_bits = a & 0b1111
print(f"Left 4 bits: {bin(left_4_bits)} or {hex(left_4_bits)}")
print(f"Right 4 bits: {bin(right_4_bits)} or {hex(right_4_bits)}")
print("")

# 0b00100010: 2x2 in S-Box = 93

matA = np.array([
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

byte_res = affine_transform(matA, vet_b, c)

sub_byte = arr_to_byte(byte_res)

print(byte_res)
print(hex(sub_byte))