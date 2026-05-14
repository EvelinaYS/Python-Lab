from main import generate_combinations

def test_generate_combinations_two_lists():
    data1 = [1, 2]
    data2 = ['a', 'b']

    expected = [
        (1, 'a'),
        (1, 'b'),
        (2, 'a'),
        (2, 'b')
    ]

    result = list(generate_combinations(data1, data2))

    assert result == expected

def test_generate_combinations_three_lists():
    data1 = [1]
    data2 = ['x', 'y']
    data3 = [True, False]

    expected = [
        (1, 'x', True),
        (1, 'x', False),
        (1, 'y', True),
        (1, 'y', False)
    ]

    result = list(generate_combinations(data1, data2, data3))

    assert result == expected

def test_generate_combinations_one_list():
    data = [1, 2, 3]

    expected = [
        (1,),
        (2,),
        (3,)
    ]

    assert list(generate_combinations(data)) == expected

def test_generate_combinations_empty():
    assert list(generate_combinations([])) == []