def task3():
    """
    Находит первые 5 чисел, больших 452021, для которых
    M % 7 == 3, где M — сумма минимального и максимального делителей
    (не считая 1 и самого числа).

    >>> task3()
    [(452025, 150678), (452029, 23810), (452034, 226019), (452048, 226026), (452062, 226033)]
    """
    result = []
    n = 452022

    while len(result) < 5:
        div = []
        for j in range(2, n):
            if n % j == 0:
                div.append(j)
        if len(div) > 0:
            m = min(div) + max(div)
            if m % 7 == 3:
                result.append((n, m))
        n += 1
    return result

if __name__ == "__main__":
    import doctest
    doctest.testmod()

    res = task3()
    for n, m in res:
        print(n, m)