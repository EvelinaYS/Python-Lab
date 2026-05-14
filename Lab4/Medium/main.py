def to_str_recursive(x):
    if not isinstance(x, list):
        return str(x) + " -> "

    if len(x) == 1:
        return str(x[0]) + " -> None"

    return to_str_recursive(x[0]) + to_str_recursive(x[1])

def to_str_iterative(x):
    s = ""
    while isinstance(x, list):
        if len(x) == 1:
            return s + str(x[0]) + " -> None"
        s += str(x[0]) + " -> "
        x = x[1]
    return s

def a_recursive(n):
    if n == 0 or n == 1:
        return 1

    return a_recursive(n - 2) + a_recursive(n - 1) / (2 ** (n - 1))

def a_iterative(n):
    if n == 0 or n == 1:
        return 1

    a0 = 1
    a1 = 1

    for i in range(2, n + 1):
        ai = a0 + a1 / (2 ** (i - 1))
        a0 = a1
        a1 = ai

    return a1