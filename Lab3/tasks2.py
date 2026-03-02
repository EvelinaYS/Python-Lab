s = 16**18 * 4**10 - 46 - 16

def count_digits_3():
    count = 0
    n = s
    while n > 0:
        if n % 4 == 3:
            count += 1
        n = n // 4
    return count

result = count_digits_3()
print(result)