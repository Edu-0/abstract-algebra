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

def multiplicative_inverse(a, b):
    return gf_egcd(a, b)[2]