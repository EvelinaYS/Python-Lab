from itertools import product


def generate_combinations(*sequences):
    for combo in product(*sequences):
        yield combo