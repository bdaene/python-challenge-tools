"""Library about factorizations of integers"""

from collections import Counter
from math import gcd
from random import randint

from primes import gen_primes_under, is_probable_prime


def factorize(n, primes=None):
    """Return a counter of each prime in the factorization of n
        :param n the integer to factorize
        :param primes the primes at least up to the square root of n in ascending order or None
    """
    if primes is None:
        primes = tuple(gen_primes_under(int(n ** 0.5) + 1))

    factorization = Counter()
    for prime in primes:
        if prime * prime > n:
            break
        d, r = divmod(n, prime)
        while r == 0:
            factorization[prime] += 1
            n = d
            d, r = divmod(n, prime)
    if n > 1:
        factorization[n] += 1
    return factorization


def _get_factor(n):
    """Return a factor of n if n is composite, n>4
    Warning : if n is prime runs forever """
    while True:
        hare = tortoise = randint(1, n - 1)
        a = randint(1, n - 1)
        power, length, divisor = 1, 1, 1
        while divisor == 1:
            if length == power:
                tortoise = hare
                power *= 2
                length = 0
            hare = (hare * hare + a) % n
            length += 1
            divisor = gcd(tortoise - hare, n)
        if divisor != n:
            return divisor


def factorize_rho(n):
    """ Pollard's Rho factorization (no prime pre-calculation needed) """
    factorization = Counter()
    while n > 1 and n % 2 == 0:
        n //= 2
        factorization[2] += 1
    if n <= 1:
        return factorization
    if is_probable_prime(n):
        factorization[n] += 1
        return factorization
    d = _get_factor(n)
    factorization.update(factorize_rho(d))
    factorization.update(factorize_rho(n // d))
    return factorization
