"""Tests for utils.py module"""

from math import comb

import pytest

from utils import comb_mod, gen_pythagorean_triples


@pytest.mark.parametrize("n, r, m", [
    (47, 15, 313),
    (79, 41, 983),
])
def test_comb_mod(n, r, m):
    assert comb(n, r) % m == comb_mod(n, r, m)


@pytest.mark.parametrize("triple, primitive", [
    [(5, 4, 3), True],
    [(5, 4, 3), False],
    [(10, 8, 6), False],
    [(493, 475, 132), True],
])
def test_gen_pythagorean_triples(triple, primitive):
    assert triple in set(gen_pythagorean_triples(triple[0], primitive))
