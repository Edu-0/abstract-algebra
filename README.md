# abstract-algebra

Small, educational scripts exploring arithmetic over **GF(2)** and **GF(2^8)** (binary polynomials), including:

- Addition in GF(2) via XOR
- Multiplication in **GF(2^8)** with reduction by an irreducible polynomial
- Polynomial multiplication/division in **GF(2)**
- Extended Euclidean Algorithm over GF(2) to compute a **multiplicative inverse** (useful in topics like AES arithmetic)

> This repo is primarily for learning/training and includes print-based demonstrations.

## Files

- `gf_operations.py`  
  Demonstrates:
  - GF(2^8) multiplication with reduction (given an irreducible polynomial `m`)
  - GF(2) polynomial multiplication (no reduction)
  - Degree of a polynomial (`deg`)
  - Polynomial long division over GF(2) (`gf2_div`)

- `multiplicative_inverse.py`  
  Computes a multiplicative inverse using the Extended Euclidean Algorithm adapted for GF(2):
  - Implements `gf2_div`, `gf2_mul`, and `gf_egcd`
  - Uses an irreducible polynomial (as modulus) and a sample element
  - Prints checks showing that `b * b^-1 = 1 (mod a)` in GF(2^8) arithmetic

- `euclid.py`  
  Contain supporting explanations of Euclidean Algorithm referenced by the other scripts.

## Brief Explanation

- In Abstract Algebra elements can be represented in many forms, as it focuses on algebraic structures where elements can be polynomials, matrices, bits, integers, etc...
- In GF(2^n) we work with polynomials, extracted from bits. For example, 10101101 would be translated to x^7 + x^5 + x^3 + x^2 + 1.
- Additions and Multiplications of coefficients are done in GF(2), meaning that every operation is done in mod 2.
  - If it was GF(3), it would be done in mod 3, and that goes on, following mod p in GF(p)
- Addition and Subtraction in GF(2) are done using XOR, and 1 + 1 = 0, which is exactly what a bitwise XOR does.
- Division is a polynomial long division using XOR for subtraction
- In GF(2^8), after multiplying, results are reduced modulo of an irreducible polynomial, or "prime polynomial," as, for a field to exist, all numbers except 0 must have multiplicative inverse, and for that to happen with every number, p as in mod p must be a prime (integer) or irreducible (polynomial).
