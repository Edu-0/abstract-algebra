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
  Appears to contain supporting explanations / earlier Euclid work referenced by the other scripts.