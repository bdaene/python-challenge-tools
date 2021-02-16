"""Tests for utils.py module"""

from math import comb

import pytest

from utils import comb_mod, gen_pythagorean_triples, timeit, DisjointSets


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


@pytest.mark.parametrize("func, args, kwargs, result", [
    (lambda: 0, (), {}, 0),
    (lambda a, b, c=3: a + b + c, (1,), {'b': 2}, 6),
])
def test_timeit(func, args, kwargs, result):
    assert timeit(func)(*args, **kwargs) == result


@pytest.mark.parametrize("elements, unions, expected_sets", [
    (set(), (), ()),
    ({1}, ((1, 1),), ({1},)),
    ({1, 2, 3}, ((1, 3),), ({1, 3}, {2})),
    ({1, 2, 3, 4, 5, 6}, ((1, 3), (2, 4), (5, 6), (6, 3)), ({1, 3, 5, 6}, {2, 4})),
    ({1, 2, 3, 4, 5, 6}, ((1, 3), (2, 4), (6, 3)), ({1, 3, 6}, {2, 4}, {5})),
])
def test_disjoint_sets(elements, unions, expected_sets):
    disjoint_sets = DisjointSets()
    for element in elements:
        disjoint_sets.make_set(element)
    for x, y in unions:
        disjoint_sets.merge(x, y)

    for disjoint_set in expected_sets:
        representatives = set(map(disjoint_sets.find, disjoint_set))
        assert len(representatives) == 1
        representative = representatives.pop()
        assert not any(disjoint_sets.find(element) == representative for element in elements - disjoint_set)
