import timeit

# O(n^2)
def naive(a, b):
    b_bin = bin(b)[2:]

    a_abs = abs(a)
    res = 0

    for i in range(len(b_bin)):
        if b_bin[len(b_bin) - 1 - i] == '1':
            res += a_abs << i
    
    negative = (a < 0 and b > 0) or (a > 0 and b < 0)
    return -res if negative else res

assert(naive(0, 25) == 0)
assert(naive(25, 0) == 0)
assert(naive(5, 5) == 25)
assert(naive(5, -5) == -25)
assert(naive(-5, 5) == -25)
assert(naive(-5, -5) == 25)

print(timeit.timeit("naive(1000000, 1000000)", globals=locals())) # five seconds