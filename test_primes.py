## attempt at writing tests
from primes import *

def test_is_2_prime():
    '''Is 2 prime?'''
    assert is_prime(2), "Two is prime!"

def test_is_23_prime():
    '''Is 23 prime?'''
    assert is_prime(23), "23 is prime!"

def test_is_0_prime():
    '''Is 0 prime?'''
    assert not is_prime(0), "0 is not prime!"

def test_is_neg5_prime():
    '''Is -5 prime?'''
    assert not is_prime(-5), "-5 is not prime!"

def test_is_1_prime():
    '''Is 1 prime?'''
    assert not is_prime(1), "1 is not prime!"

def test_list_primes_10():
    '''Primes below 10'''
    assert list_primes_below(10) == [2,3,5,7], "Wrong list for 10!"

def test_list_primes_3():
    '''Primes below 3'''
    assert list_primes_below(3) == [2,3], "Wrong list for 3!"

def test_list_primes_neg1():
    '''Primes below -1'''
    assert list_primes_below(-1) == [], "Wrong list for -1!"

def test_list_primes_23():
    '''Primes below 23'''
    assert list_primes_below(23) == [2,3,5,7,11,13,17,19,23], "Wrong list for 23!"

def test_sum_primes_10():
    '''Sum primes below 10'''
    assert sum_primes_below(10) == 17, "Wrong sum for 10!"

def test_sum_primes_3():
    '''Sum Primes below 3'''
    assert sum_primes_below(3) == 5, "Wrong sum for 3!"

def test_sum_primes_neg1():
    '''Sum Primes below -1'''
    assert sum_primes_below(-1) == 0, "Wrong sum for -1!"

def test_sum_primes_23():
    '''Sum Primes below 23'''
    assert sum_primes_below(23) == sum([2,3,5,7,11,13,17,19,23]), "Wrong sum for 23!"

def test_sum_primes_28():
    '''Sum Primes below 28'''
    assert sum_primes_below(28) == sum([2,3,5,7,11,13,17,19,23]), "Wrong sum for 28!"

def test_sum_primes_10000():
    '''Sum Primes below 10000'''
    assert sum_primes_below(10000) == 5736396, "Wrong sum for 10K!"
