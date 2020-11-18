"""Library containing tools that do not fit in specialized libraries"""

from math import comb


def comb_mod(n, r, mod):
    """Returns comb(n, r) % mod using Lucas theorem. mod has to be prime."""
    c = 1
    while r > 0:
        r, rm = divmod(r, mod)
        n, nm = divmod(n, mod)
        c *= comb(rm, nm)
        c %= mod
    return c
