from math import sqrt
from collections import Counter

def memoize(f):
    results = {}
    def helper(x):
        if x not in results:            
            results[x] = f(x)
        return results[x]
    return helper

primes = []
def gen_prime():
    for i in primes:
        yield i

    if not primes or primes[-1] < 2:
        i = 2
        primes.append(i)
        yield i
    
    i += 1
    if i % 2 == 0:
        i += 1
    while True:
        sqrt_i = int(sqrt(i))
        for j in primes:
            if j > sqrt_i:
                primes.append(i)
                yield i
                break
            elif i % j == 0:
                break                
        i += 2

def get_primes():
    return primes

def old_gen_prime():
    primes = []
    i = 2
    primes.append(i)
    yield primes[-1]
    
    i = 3
    while True:
        for j in primes:
            if j * j > i:
                primes.append(i)
                yield primes[-1]
                break
            elif i % j == 0:
                break                
        i += 2

def old_get_factors(x):
    factors = []
    f = 2
    while f * f <= x:
        while x % f == 0:
            factors.append(f)
            x /= f
        f += 1
    if x != 1:
        factors.append(x)
    return factors

def get_factors2(x):
    sqrt_x = int(sqrt(x))
    factors = []
    for p in gen_prime():
        while p <= sqrt_x and x % p == 0:
            factors.append(p)
            x //= p
            sqrt_x = int(sqrt(x))
        if p * p > x:
            break
    if x != 1:
        factors.append(x)
    return factors

def greatest_common_divisor(a, b):
    while True:
        c = a % b
        if c == 0:
            return b
        a, b = b, c

def get_factors3(x):
    factors = []
    for f in gen_prime():
        while f * f <= x and x % f == 0:
            factors.append(f)
            x //= f
        if f * f > x:
            break
    if x != 1:
        factors.append(x)
    return factors

_factors_cache = {}
def get_factors4(x):
    if x in _factors_cache:
        return _factors_cache[x]
    original_x = x
    factors = []
    for f in gen_prime():
        while f * f <= x and x % f == 0:
            factors.append(f)
            x //= f
            # if x in _factors_cache:
            #     factors.extend(_factors_cache[x])
            #     _factors_cache[original_x] = factors
            #     return _factors_cache[x]
        if f * f > x:
            break
    if x != 1:
        factors.append(x)
    _factors_cache[original_x] = factors
    return factors

@memoize
def get_factors5(x):
    factors = []
    for f in gen_prime():
        while f * f <= x and x % f == 0:
            factors.append(f)
            x //= f
        if f * f > x:
            break
    if x != 1:
        factors.append(x)
    return factors

@memoize
def get_factors(x):
    factors = []
    for f in gen_prime():
        while f * f <= x and x % f == 0:
            factors.append(f)
            x //= f
        if f * f > x:
            break
    if x != 1:
        factors.append(x)
    return factors

def canonical_decomposition2(x):
    '''
    Returns dictionary where keys are primes and values are exponents.

    [(prime, p[prime]) for prime in sorted(p)]
    '''
    factors = {}
    for factor in get_factors2(x):
        try:
            factors[factor] += 1
        except KeyError:
            factors[factor] = 1
    return factors

def canonical_decomposition3(x):
    '''
    Returns dictionary where keys are primes and values are exponents.

    [(prime, p[prime]) for prime in sorted(p)]
    '''
    factors = {}
    for factor in get_factors2(x):
        if factor not in factors:
            factors[factor] = 0
        factors[factor] += 1
    return factors

def canonical_decomposition4(x):
    '''
    Returns dictionary where keys are primes and values are exponents.

    [(prime, p[prime]) for prime in sorted(p)]
    '''
    factors = Counter()
    for factor in get_factors2(x):
        factors[factor] += 1
    return factors

def canonical_decomposition5(x):
    factors = Counter()
    for f in gen_prime():
        while f * f <= x and x % f == 0:
            factors[f] += 1
            x //= f
        if f * f > x:
            break
    if x != 1:
        factors[x] += 1
    return factors

def canonical_decomposition(x):
    factors = {}
    for f in gen_prime():
        while f * f <= x and x % f == 0:
            if f not in factors:
                factors[f] = 0
            factors[f] += 1
            x //= f
        if f * f > x:
            break
    if x != 1:
        if x not in factors:
            factors[x] = 0
        factors[x] += 1
    return factors

def gen_triangular():
    i = 0
    n = 1
    while True:
        i += n
        yield i
        n += 1

def direct_fibonacci(n):
    '''
    This is likely not accurate for other than small n.
    '''
    phi = (sqrt(5) + 1.) / 2.
    return int(round((phi ** n) / sqrt(5)))   

from math import sqrt, log, ceil
phi = (sqrt(5) + 1.) / 2.
def term_of_ndigits_fibonacci(ndigits):
    return int(ceil((log(sqrt(5)) + (ndigits - 1) * log(10)) / log(phi)))

def gen_fibonacci():
    a, b = 0, 1
    while True:
        a, b = b, a + b
        yield b

def gen_even(gen):
    for i in gen:
        if i%2 == 0:
            yield i

def gen_lte(gen, n):
    for i in gen:
        if i > n:
            break
        yield i

def gen_lt(gen, n):
    for i in gen:
        if i >= n:
            break
        yield i

def gen_n(gen, n):
    for i in gen:
        if n <= 0:
            break
        yield i
        n -= 1

def make_square_roots(n):
    return map((lambda x: (x*x, x)), range(n))

def product(x):
    n = 1
    for i in x:
        n *= i
    return n
