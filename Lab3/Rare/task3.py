def task3():
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

res = task3()
for n, m in res:
    print(n, m)