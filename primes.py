"""Library about primes sieves and primality tests"""


def gen_primes_under(n):
    """Returns all primes under n in increasing order"""
    if n < 3:
        return
    n2 = n >> 1
    yield 2
    primes = [True] * n2
    primes[0], i = False, 1
    while i < n2:
        if primes[i]:
            p = (i << 1) + 1
            if p * p > n:
                break
            yield p
            for m in range(i * (i + 1) << 1, n2, p):
                primes[m] = False
        i += 1
    while i < n2:
        if primes[i]:
            yield (i << 1) + 1
        i += 1


def gen_primes():
    """Generate all primes in increasing order"""
    yield 2
    found, offset, sieve = [], 1, [True] * 3
    while True:
        # Collect the primes
        for i, prime in enumerate(sieve):
            if prime:
                p = (offset + i) * 2 + 1
                yield p
                found.append(offset + i)

        # Move the sieve to next range
        offset += len(sieve)
        sieve = [True] * min(offset * (offset * 2 - 1), 1000000)  # Capped to avoid growing over memory
        for i in found:
            s = i * (i + 1) * 2 - offset
            if s > len(sieve):
                break
            p = i * 2 + 1
            if s < 0:
                s += ((p - 1 - s) // p) * p
            for m in range(s, len(sieve), p):
                sieve[m] = False


def is_probable_prime(n, ar=None):
    """Return True if n1 is prime and probably False if n1 is composed.
     Use the Rabin-Miller test.
     In order to be sure that n1 is prime, the choice or ar should be made as
     if n1 <           1,373,653, it is enough to test ar = {2, 3};
     if n1 <           9,080,191, it is enough to test ar = {31, 73};
     if n1 <       4,759,123,141, it is enough to test ar = {2, 7, 61};
     if n1 <   2,152,302,898,747, it is enough to test ar = {2, 3, 5, 7, 11};
     if n1 <   3,474,749,660,383, it is enough to test ar = {2, 3, 5, 7, 11, 13};
     if n1 < 341,550,071,728,321, it is enough to test ar = {2, 3, 5, 7, 11, 13, 17}.
     if n1 <      at least 2**64, it is enough to test ar = {2, 325, 9375, 28178, 450775, 9780504, 1795265022}.
    """
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    if n < 9:
        return True
    if n % 3 == 0:
        return False
    if n % 5 == 0:
        return False
    # Default ar
    if not ar:
        if n < 1373653:
            ar = (2, 3)
        elif n < 9080191:
            ar = (31, 73)
        elif n < 4759123141:
            ar = (2, 7, 61)
        elif n < 2152302898747:
            ar = (2, 3, 5, 7, 11)
        elif n < 3474749660383:
            ar = (2, 3, 5, 7, 11, 13)
        elif n < 341550071728321:
            ar = (2, 3, 5, 7, 11, 13, 17)
        else:
            ar = (2, 325, 9375, 28178, 450775, 9780504, 1795265022)

    for a in ar:
        if a == n:
            continue
        t, u = 0, n - 1
        while (u & 1) == 0:
            t += 1
            u >>= 1

        xi1 = pow(a, u, n)

        for _ in range(0, t):
            xi2 = (xi1 * xi1) % n
            if xi2 == 1 and xi1 != 1 and xi1 != n - 1:
                return False
            xi1 = xi2

        if xi1 != 1:
            return False
    return True


def is_prime(n):
    """Return true if n1 is prime else false."""
    if n < 2:
        return False
    if n < 4:
        return True
    if n % 2 == 0:
        return False
    if n < 9:
        return True
    if n % 3 == 0:
        return False

    for i in range(5, int(n ** 0.5) + 1, 6):
        if n % i == 0:
            return False
        if n % (i + 2) == 0:
            return False

    return True
