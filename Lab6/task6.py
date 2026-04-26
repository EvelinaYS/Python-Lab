from itertools import product

def generate_combinations(*sequences):
    for combo in product(*sequences):
        yield combo

for c in generate_combinations([1, 2], ['a', 'b'], ['X', 'Y'], [True, False]):
    print(c)