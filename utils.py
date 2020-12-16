"""Library containing tools that do not fit in specialized libraries"""

from functools import wraps
from math import comb, gcd
from sys import stdout
from time import perf_counter


def comb_mod(n, r, mod):
    """Returns comb(n, r) % mod using Lucas theorem. mod has to be prime."""
    c = 1
    while r > 0:
        r, rm = divmod(r, mod)
        n, nm = divmod(n, mod)
        c *= comb(nm, rm)
        c %= mod
    return c


def gen_pythagorean_triples(max_z, primitive=False):
    """Generate pythagorean triple (z,y,x) such that (z*z = y*y+x*x) and z>y>x>0"""
    for m in range(2, int(max_z ** 0.5) + 1):
        m2 = m * m
        for n in range(m % 2 + 1, min(int((max_z - m2) ** 0.5) + 1, m), 2):
            if gcd(m, n) == 1:
                n2 = n * n
                x, y, z = m2 - n2, 2 * m * n, m2 + n2
                if x > y:
                    x, y = y, x
                if primitive:
                    yield z, y, x
                else:
                    for k in range(1, max_z // z + 1):
                        yield z * k, y * k, x * k


def timeit(func, file=stdout):
    """Allows to time an execution while still getting the result. With a simple decorator."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        clock = perf_counter()
        result = func(*args, **kwargs)
        print(f"Execution of {func.__name__} took {(perf_counter() - clock) * 1000:.3f}ms.", file=file)
        print(f"Result: {result}", file=file)
        return result

    wrapper.func = func
    return wrapper
