def to_str(x):
    s = ""
    while isinstance(x, list):
        if len(x) == 1:
            s += str(x[0]) + " -> None"
            return s
        s += str(x[0]) + " -> "
        x = x[1]
    return s

print(to_str([1, [2, [3, [4, [5]]]]]))