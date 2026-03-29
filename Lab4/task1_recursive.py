def to_str(x):
    if not isinstance(x, list):
        return str(x) + " -> "

    if len(x) == 1:
        return str(x[0]) + " -> None"

    return to_str(x[0]) + to_str(x[1])

print(to_str([1, [2, [3, [4, [5]]]]]))