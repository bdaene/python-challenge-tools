"""Tests for euclide.py module"""

import pytest

from euclide import gcd, gcde, inv_mod, get_inv_mods, solve_chinese_remainders


@pytest.mark.parametrize("a, b, d", [
    (48, 67, 1),
    (34, 17, 17),
    (0, 24, 24),
    (37, 37, 37),
    (5, 7, 1),
])
def test_gcd(a, b, d):
    assert d == gcd(a, b)
    assert d == gcd(b, a)
    assert a % d == 0
    assert b % d == 0


@pytest.mark.parametrize("a, b", [
    (7, 0),
    (78, 13),
    (2, 3),
    (20, 30),
])
def test_gcde(a, b):
    r, u, v = gcde(a, b)
    assert r == u * a + v * b
    assert r == gcd(a, b)


@pytest.mark.parametrize("a, m", [
    (3, 6),
    (13, 17),
    (31, 7),
    (20, 20),
])
def test_inv_mod(a, m):
    i = inv_mod(a, m)
    if gcd(a, m) == 1:
        assert i * a % m == 1
    else:
        assert i is None


@pytest.mark.parametrize("m, n", [
    (7, None),
    (13, 5),
    (17, None),
    (31, None),
])
def test_get_inv_mods(m, n):
    inv = get_inv_mods(m, n)
    if n is None:
        assert len(inv) == m
    else:
        assert len(inv) == n

    assert None not in inv[1:]
    assert all(a * b % m == 1 for a, b in enumerate(inv[1:], 1))


@pytest.mark.parametrize("remainders, expected_result", [
    ([], 0),
    ([(7, 13)], 7),
    ([(31 % 13, 13), (31 % 19, 19)], 31)
])
def test_chinese_remainders(remainders, expected_result):
    assert expected_result == solve_chinese_remainders(remainders)
