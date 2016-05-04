
def is_palindrome(num):
    '''Converts num to string, reverses string and checks equality.'''
    rep = str(num)
    if rep == rep[::-1]:
        return True
    else:
        return False

space = [x*y for x in range(100,1000) for y in range(100,1000)]
palindromes = [num for num in space if is_palindrome(num)]
print('Answer: {}'.format(max(palindromes)))
