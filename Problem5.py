## prime factorization y'all
ans = 5*7*9*11*13*16*17*19
print('Math Answer : {}'.format(ans))

## if you dont know primes at all
import sys
upp_bound = sys.maxsize # largest number machine cares about

divs = [5,7,9,11,13,16,17,19]

def recurse(num, ls):
    '''Recursively moves through given list to check remainders.
       First copies the list via a slice, and then proceeds to iteratively pop from the copy.'''

    copy = ls[:] # slicing a list produces a copy
    if len(copy)>0:

        ## if remainder is 0 on last item, move on
        if not (num % copy.pop()):
            return recurse(num, copy)

        ## else we're done here
        else:
            return False

    else:
        return True # empty list == base case

## using a comprehension to produce an iterator; calling next initializes the iterator
## and consequently we stop at the first value, i.e., the min
ans = next(i for i in range(20,upp_bound,20) if recurse(i, divs))
print('Programming Answer : {}'.format(ans))
