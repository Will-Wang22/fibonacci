def inner(n):
    "Returns (F(n-1), F(n))"
    if n == 0:
        return (0, 1)
    else:
        pair = inner(n - 1)
        return (pair[1], pair[0] + pair[1])

def fib(n):
    return inner(n)[1]