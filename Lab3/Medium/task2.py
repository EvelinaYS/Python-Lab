def task2():
    """
    Находит количество цифр 3 в четверичной записи числа:
    16^18 * 4^10 - 46 - 16.

    >>> task2()
    43
    """
    n = 16 ** 18 * 4 ** 10 - 46 - 16
    count = 0

    while n > 0:
        if n % 4 == 3:
            count += 1
        n //= 4
    return count

if __name__ == "__main__":
    import doctest
    doctest.testmod()

    print(task2())