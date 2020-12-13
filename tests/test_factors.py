"""Tests for factors.py module"""

from collections import Counter
from functools import reduce

import pytest

from factors import factorize, factorize_rho, get_factorization_under


@pytest.mark.parametrize("n, factors", [
    (0, Counter()),
    (1, Counter()),
    (7 ** 2, Counter({7: 2})),
    (3 * 5 * 7 * 11 * 13, Counter({3: 1, 5: 1, 7: 1, 11: 1, 13: 1})),
])
def test_factorize(n, factors):
    assert factors == factorize(n)


@pytest.mark.parametrize("n, factors", [
    (0, Counter()),
    (1, Counter()),
    (7 ** 2, Counter({7: 2})),
    (3 * 5 * 7 * 11 * 13, Counter({3: 1, 5: 1, 7: 1, 11: 1, 13: 1})),
    (2 ** 7 * 1559521 * 86453537, Counter({2: 7, 1559521: 1, 86453537: 1}))
])
def test_factorize_rho(n, factors):
    assert factors == factorize_rho(n)


@pytest.mark.parametrize("n", [10, 1000])
def test_get_factorization_under(n):
    factors = get_factorization_under(n)
    assert all(
        n == reduce(lambda a, b: a * b[0] ** b[1], factors[n].items(), 1) for n in range(1, len(factors)))
