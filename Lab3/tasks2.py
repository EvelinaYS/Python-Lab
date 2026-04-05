def task2():
    n = 16 ** 18 * 4 ** 10 - 46 - 16

    count = 0
    while n > 0:
        if n % 4 == 3:
            count += 1
        n = n // 4
    return count

result = task2()
print(result)