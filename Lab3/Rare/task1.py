from itertools import product

def task1():
    letters = ['Н', 'А', 'С', 'Т', 'Я']
    count = 0
    for letter in product(letters, repeat = 6):
        if letter.count('А') <= 1 and letter.count('Я') <= 1:
            count += 1
    return count

result = task1()
print(result)