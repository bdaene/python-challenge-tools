"""Library about GCD Euclide's algorithms and applications"""


def gcd(a, b):
    """Returns the greatest common divisor of a and b."""
    # It is better to use math.gcd.
    while a:
        a, b = b % a, a
    return b


def gcde(a, b):
    """Extended Euclide's GCD algorithm."""
    # The equalities r = a*u+b*v and r2 = a*u2+b*v2 are the loop invariants
    r, u, v, r2, u2, v2 = a, 1, 0, b, 0, 1
    while r:
        q = r2 // r
        r, u, v, r2, u2, v2 = r2 - q * r, u2 - q * u, v2 - q * v, r, u, v
    return r2, u2, v2


def inv_mod(a, m):
    """Returns the inverse of a modulo m if it exists."""
    r, u, v = gcde(a, m)
    if r == 1:
        return u % m


def get_inv_mods(m, n=None):
    """Get the inverses of {0..n-1} modulo m. m must be prime."""
    if n is None:
        n = m
    inv = [None, 1]
    for i in range(2, n):
        d, r = divmod(m, i)
        inv.append(-d * inv[r] % m)
    return inv
