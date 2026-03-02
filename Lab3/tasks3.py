def find_numbers():
    found_numbers = []
    count = 0
    for n in range(452022, 1000000):
        div = []
        for j in range(2,n):
            if n % j == 0:
                div.append(j)
                if len(div) >= 2:
                    m = div[0] + div[-1]
        if m % 7 == 3:
            count += 1
            found_numbers.append((n , m))
        if count == 5:
            break
    return found_numbers

result = find_numbers()
for n, m in result:
    print(n, m)