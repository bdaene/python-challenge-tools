"""Tests for primes.py module"""

import pytest

from primes import gen_primes_under, gen_primes, is_probable_prime, is_prime


@pytest.mark.parametrize("n", [
    1000,
])
def test_gen_primes_under(n):
    primes = tuple(gen_primes_under(n))
    for p in range(2, n):
        assert all(p % d != 0 for d in range(2, int(p ** 0.5) + 1)) == (p in primes)


@pytest.mark.parametrize("n", [
    100000,
])
def test_gen_primes(n):
    for p1, p2 in zip(gen_primes(), gen_primes_under(n)):
        assert p1 == p2


@pytest.mark.parametrize("n, prime", [
    (13, True),
    (14, False),
    (484845637, True),
    (484846079 * 484844609, False)
])
def test_is_probable_prime(n, prime):
    assert prime == is_probable_prime(n)


@pytest.mark.parametrize("n", [
    100000,
])
def test_is_prime(n):
    primes = set(gen_primes_under(n))
    for p in range(2, n):
        assert is_prime(p) == (p in primes)
