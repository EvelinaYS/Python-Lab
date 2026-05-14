def a(n):
    if n == 0 or n == 1:
        return 1

    a0 = 1
    a1 = 1

    for i in range(2, n + 1):
        ai = a0 + a1 / (2 ** (i - 1))
        a0 = a1
        a1 = ai

    return a1

print(a(5))