## (x+y)^2 - x^2-y^2 = 2xy

def diff(N):
    '''function to compute
    1^2 + 2^2 + ... + N^2 - (1+...+N)^2
    '''

    return sum([x*y for x in range(1,N+1) for y in range(1,N+1) if x != y])

print('Answer: {}'.format(diff(100)))
