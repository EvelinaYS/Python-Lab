from itertools import product

def task1():
    """
    Подсчитывает количество 6-буквенных кодов из букв Н, А, С, Т, Я,
    где каждая гласная (А, Я) встречается не более одного раза.

    >>> task1()
    6075
    """
    letters = ['Н', 'А', 'С', 'Т', 'Я']
    count = 0
    for code in product(letters, repeat=6):
        if code.count('А') <= 1 and code.count('Я') <= 1:
            count += 1
    return count

if __name__ == "__main__":
    import doctest
    doctest.testmod()

    print(task1())