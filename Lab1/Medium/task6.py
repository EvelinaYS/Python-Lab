def run():
    zoo = ['lion', 'kangaroo', 'elephant', 'monkey']

    zoo.insert(1, 'bear')
    print(zoo)

    birds = ['rooster', 'ostrich', 'lark']

    zoo.extend(birds)
    print(zoo)

    zoo.remove('elephant')
    print(zoo)

    print(f'Лев сидит в клетке {zoo.index("lion") + 1}')
    print(f'Жаворонок сидит в клетке {zoo.index("lark") + 1}')

if __name__ == '__main__':
    run()