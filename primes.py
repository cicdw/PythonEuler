'''Functions related to prime numbers, just because I know this is going to come up all the damn time.'''

import math

def is_prime(n):
    '''Function for checking primality.'''

    if n<2:
        return False

    if n==2:
        return True

    if n%2==0:
        return False
    
    try:
        div = next(d for d in range(3,round(math.sqrt(n)+1),2) if n%d==0)
        return False
    except StopIteration:
        return True

def sum_primes_below(n):
    '''Returns the sum of primes <= n'''

    if n<2:
        return 0
    elif n==2:
        return 2

    sieve = [True]*(n+1) # will treat index as actual number
    sieve[0], sieve[1] = False, False # just for my sanity

    def filter_out(num):
        '''Filters out all multiples of num.'''
        for div in range(2*num, n+1, num):
            sieve[div] = False

    res = 0
    for base in range(2,n+1):
        if sieve[base]:
            filter_out(base)
            res += base

    return res

def list_primes_below(n):
    '''Returns a list of primes <= n'''

    if n<2:
        return []
    elif n==2:
        return [2]

    sieve = [True]*(n+1) # will treat index as actual number
    sieve[0], sieve[1] = False, False # just for my sanity

    def filter_out(num):
        '''Filters out all multiples of num.'''
        for div in range(2*num, n+1, num):
            sieve[div] = False

    res = []
    for base in range(2,n+1):
        if sieve[base]:
            filter_out(base)
            res.append(base)

    return res
